import * as fs from 'node:fs';
import { marked } from 'marked';
import { resolveProjectFile, estimateReadingTime, countWords } from './book';

export interface RenderedChapter {
  htmlContent: string;
  footnotesHtml: string;
  refsHtml: string;
  readingTime: number;
  wordCount: number;
}

interface Citation {
  author: string;
  year: string;
  title: string;
  url?: string;
}

function loadCitations(): Record<string, Citation> {
  const data: Record<string, Citation> = {};
  try {
    const bibContent = fs.readFileSync(resolveProjectFile('references.bib'), 'utf-8');
    const entryRegex = /@\w+\s*\{\s*([^,]+)\s*,([^@]*?)(?=\n@|\n*$)/gs;
    let match;
    while ((match = entryRegex.exec(bibContent)) !== null) {
      const key = match[1].trim();
      const entry = match[2];
      const getField = (field: string) => {
        const m = entry.match(new RegExp(`${field}\\s*=\\s*[{"]([^}"]*)[}"]`, 'i'));
        return m ? m[1].replace(/\{([^}]+)\}/g, '$1').replace(/\s+/g, ' ').trim() : '';
      };
      data[key] = {
        author: getField('author').replace(/^\{|\}$/g, '').split(',')[0].split(' and ')[0],
        year: getField('year'),
        title: getField('title'),
        url: getField('url') || (getField('doi') ? `https://doi.org/${getField('doi')}` : undefined),
      };
    }
  } catch (e) {
    /* references are optional */
  }
  return data;
}

const concepts: Record<string, { title: string; desc: string }> = {
  'guy-orcutt': { title: 'Guy Orcutt', desc: 'Father of microsimulation (1917–2006)' },
  policyengine: { title: 'PolicyEngine', desc: 'Open-source tax-benefit microsimulation platform' },
  openfisca: { title: 'OpenFisca', desc: 'Open-source platform for modeling tax and benefit systems' },
  taxsim: { title: 'TAXSIM', desc: 'NBER tax microsimulation model' },
  'axiom-foundation': { title: 'The Axiom Foundation', desc: 'Open, verified encodings of public policy (RuleSpec)' },
  'thesis-institute': { title: 'Thesis Institute', desc: 'Open, graded forecasts of government metrics' },
  populace: { title: 'populace', desc: 'Calibrated population microdata commons' },
  'ubi-center': { title: 'UBI Center', desc: 'Think tank for universal basic income research' },
  'rules-as-code': { title: 'Rules as Code', desc: 'Movement to express legislation in machine-executable form' },
};

const esc = (s: string) =>
  s
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');

// Inline footnotes ^[…] with bracket counting (they can contain [marks]).
function extractFootnotes(text: string): { text: string; notes: string[] } {
  const notes: string[] = [];
  let out = '';
  let i = 0;
  while (i < text.length) {
    if (text[i] === '^' && text[i + 1] === '[') {
      let depth = 1;
      let j = i + 2;
      while (j < text.length && depth > 0) {
        if (text[j] === '[') depth++;
        else if (text[j] === ']') depth--;
        j++;
      }
      notes.push(text.slice(i + 2, j - 1));
      out += `<sup class="fn" id="fnref-${notes.length}"><a href="#fn-${notes.length}" style="color:inherit;text-decoration:none">${notes.length}</a></sup>`;
      i = j;
    } else {
      out += text[i];
      i++;
    }
  }
  return { text: out, notes };
}

export function renderChapter(file: string): RenderedChapter {
  const citationData = loadCitations();
  const usedCitations: string[] = [];

  // Shared inline transforms: draft marks, citations, wiki-links.
  function transformInline(text: string): string {
    // Draft marks first, so the citation pass can't eat them.
    text = text.replace(/\[NEEDS CITATION:?\s*([^\]]*)\]/g, (_, note) => {
      const tip = note.trim() ? esc(note.trim()) : 'source to be added';
      return `<span class="mark mark--cite" title="${tip}">citation pending</span>`;
    });
    text = text.replace(/\[VERIFY(?: with [^:\]]+)?:?\s*([^\]]*)\]/g, (_, note) => {
      const tip = note.trim() ? esc(note.trim()) : 'fact to re-verify before publication';
      return `<span class="mark mark--verify" title="${tip}">to verify</span>`;
    });

    // Pandoc citations: [@key; @other], moving trailing punctuation inside.
    text = text.replace(/\[([^\]]*@[\w:-][^\]]*)\]([.,;:!?])?/g, (_, group, punct) => {
      const refs = [...group.matchAll(/@([\w:-]+)/g)]
        .map((m: RegExpMatchArray) => m[1])
        .filter((key: string) => citationData[key]);
      if (refs.length === 0) return punct || '';
      const sup = refs
        .map((key: string) => {
          const cite = citationData[key];
          if (!usedCitations.includes(key)) usedCitations.push(key);
          const num = usedCitations.indexOf(key) + 1;
          return `<sup class="cite" data-tip="${esc(`${cite.author}, ${cite.year}`)}" data-url="${cite.url || ''}">[${num}]</sup>`;
        })
        .join('');
      return punct ? `${punct}${sup}` : sup;
    });

    // Wiki-links.
    text = text.replace(/\[\[([^\]]+)\]\]/g, (_, entity) => {
      const cslug = entity.toLowerCase().replace(/\s+/g, '-');
      const concept = concepts[cslug];
      if (concept) return `<span class="concept" data-tip="${esc(concept.desc)}">${concept.title}</span>`;
      return entity.replace(/-/g, ' ');
    });

    return text;
  }

  let htmlContent = '';
  let footnotesHtml = '';
  let readingTime = 0;
  let wordCount = 0;

  try {
    let content = fs.readFileSync(resolveProjectFile(file), 'utf-8');
    readingTime = estimateReadingTime(content);
    wordCount = countWords(content);

    // Authoring artifacts the reader never shows.
    content = content
      .replace(/<!--[\s\S]*?-->/g, '')
      .replace(/^#\s+.+$/m, '') // the H1: rendered by the chapter header
      .replace(/\{\{<\s*include\s+[^>]+>\}\}/g, '')
      .replace(/^## References\s*$/gm, '');

    const extracted = extractFootnotes(content);
    content = transformInline(extracted.text);
    const notes = extracted.notes.map((n) => transformInline(n));

    marked.setOptions({ gfm: true, breaks: false });
    htmlContent = marked.parse(content) as string;
    // Wide content scrolls inside its own container.
    htmlContent = htmlContent
      .replaceAll('<table>', '<div class="table-wrap"><table>')
      .replaceAll('</table>', '</table></div>');

    if (notes.length > 0) {
      footnotesHtml =
        '<div class="footnotes"><ol>' +
        notes
          .map(
            (n, idx) =>
              `<li id="fn-${idx + 1}">${marked.parseInline(n) as string} <a href="#fnref-${idx + 1}" style="text-decoration:none">↩</a></li>`
          )
          .join('') +
        '</ol></div>';
    }
  } catch (error) {
    console.error(`Error reading chapter file: ${file}`, error);
    htmlContent = '<p>This chapter could not be loaded.</p>';
  }

  // References list, in order of first citation.
  let refsHtml = '';
  if (usedCitations.length > 0) {
    refsHtml =
      '<div class="refs"><h3>References</h3><ol>' +
      usedCitations
        .map((key) => {
          const c = citationData[key];
          if (!c) return '';
          const label = `${c.author} (${c.year}). ${c.title}.`;
          return `<li>${c.url ? `<a href="${c.url}" target="_blank" rel="noopener">${esc(label)}</a>` : esc(label)}</li>`;
        })
        .join('') +
      '</ol></div>';
  }

  return { htmlContent, footnotesHtml, refsHtml, readingTime, wordCount };
}
