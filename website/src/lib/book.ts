import * as fs from 'node:fs';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';
import { parse as parseYaml } from 'yaml';

export interface Chapter {
  slug: string;
  title: string;
  file: string;
  words?: number;
  part?: string;
  partNumber?: number;
  chapterNumber?: number;
}

export interface Part {
  title: string;
  number: number;
  chapters: Chapter[];
}

export interface BookStructure {
  title: string;
  subtitle: string;
  author: string;
  frontMatter: Chapter[];
  parts: Part[];
}

type QuartoChapterEntry =
  | string
  | {
      part?: string;
      chapters?: string[];
    };

interface QuartoAuthor {
  name?: string;
}

interface QuartoConfig {
  book?: {
    title?: string;
    subtitle?: string;
    author?: string | string[] | QuartoAuthor | QuartoAuthor[];
    chapters?: QuartoChapterEntry[];
  };
}

function findRepoRoot(): string {
  const bundledCandidate = path.dirname(
    fileURLToPath(new URL('../../../_quarto.yml', import.meta.url))
  );
  const cwd = process.cwd();
  const candidates = [bundledCandidate, path.resolve(cwd, '..'), cwd];

  for (const candidate of candidates) {
    if (fs.existsSync(path.join(candidate, '_quarto.yml'))) {
      return candidate;
    }
  }

  throw new Error('Unable to locate repo-root _quarto.yml from website build context');
}

export const repoRoot = findRepoRoot();
const quartoPath = path.join(repoRoot, '_quarto.yml');

export function resolveProjectFile(file: string): string {
  return path.resolve(repoRoot, file);
}

function loadQuartoConfig(): QuartoConfig {
  const config = parseYaml(fs.readFileSync(quartoPath, 'utf-8')) as QuartoConfig;

  if (!config.book?.chapters?.length) {
    throw new Error('_quarto.yml is missing book.chapters entries');
  }

  return config;
}

function slugFromFile(file: string): string {
  return path.basename(file, path.extname(file)).replace(/^\d+-/, '');
}

function readDocumentTitle(file: string): string | null {
  const content = fs.readFileSync(resolveProjectFile(file), 'utf-8');
  const match = content.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : null;
}

function fallbackTitleFromSlug(slug: string): string {
  return slug
    .split('-')
    .map((segment) => segment.charAt(0).toUpperCase() + segment.slice(1))
    .join(' ');
}

function chapterFromFile(file: string, overrides?: Partial<Chapter>): Chapter {
  const slug = slugFromFile(file);

  if (!fs.existsSync(resolveProjectFile(file))) {
    throw new Error(`_quarto.yml references a missing file: ${file}`);
  }

  const content = fs.readFileSync(resolveProjectFile(file), 'utf-8');
  const titleMatch = content.match(/^#\s+(.+)$/m);
  const title = (titleMatch ? titleMatch[1].trim() : fallbackTitleFromSlug(slug))
    .replace(/^Chapter\s+\d+:\s*/i, '');

  return {
    slug,
    title,
    file,
    words: countWords(content),
    ...overrides,
  };
}

function partTitleFromConfig(part?: string): string {
  return (part ?? '').replace(/^Part\s+[A-Z0-9]+\s*:\s*/i, '').trim();
}

function readAuthor(author: QuartoConfig['book'] extends { author?: infer T } ? T : never): string {
  if (typeof author === 'string') {
    return author;
  }

  if (Array.isArray(author)) {
    const first = author[0];
    if (typeof first === 'string') {
      return first;
    }
    return first?.name?.trim() || 'Max Ghenis';
  }

  if (author && typeof author === 'object') {
    return author.name?.trim() || 'Max Ghenis';
  }

  return 'Max Ghenis';
}

function loadBookStructure(): BookStructure {
  const book = loadQuartoConfig().book!;
  const frontMatter: Chapter[] = [];
  const parts: Part[] = [];
  let chapterNumber = 0;

  for (const entry of book.chapters ?? []) {
    if (typeof entry === 'string') {
      // index.md is the site landing page, not a readable chapter.
      if (path.normalize(entry) === 'index.md') continue;
      frontMatter.push(chapterFromFile(entry));
      continue;
    }

    const partNumber = parts.length + 1;
    const partTitle = partTitleFromConfig(entry.part) || `Part ${partNumber}`;
    const chapters = (entry.chapters ?? []).map((file) => {
      chapterNumber += 1;
      return chapterFromFile(file, {
        part: partTitle,
        partNumber,
        chapterNumber,
      });
    });

    if (chapters.length > 0) {
      parts.push({
        title: partTitle,
        number: partNumber,
        chapters,
      });
    }
  }

  if (frontMatter.length === 0 || parts.length === 0) {
    throw new Error('Failed to derive book structure from _quarto.yml');
  }

  return {
    title: book.title?.trim() || 'Society in Silico',
    subtitle: book.subtitle?.trim() || '',
    author: readAuthor(book.author),
    frontMatter,
    parts,
  };
}

// Website routing and navigation derive from the same TOC Quarto uses to build the book.
export const bookStructure: BookStructure = loadBookStructure();

export function getAllChapters(): Chapter[] {
  const chapters: Chapter[] = [...bookStructure.frontMatter];
  for (const part of bookStructure.parts) {
    chapters.push(...part.chapters);
  }
  return chapters;
}

export function getChapterBySlug(slug: string): Chapter | undefined {
  return getAllChapters().find((chapter) => chapter.slug === slug);
}

export function getChapterNavigation(slug: string): {
  prev: Chapter | null;
  next: Chapter | null;
} {
  const chapters = getAllChapters();
  const currentIndex = chapters.findIndex((ch) => ch.slug === slug);

  return {
    prev: currentIndex > 0 ? chapters[currentIndex - 1] : null,
    next: currentIndex < chapters.length - 1 ? chapters[currentIndex + 1] : null,
  };
}

export function getChapterPosition(slug: string): {
  current: number;
  total: number;
} {
  const chapters = getAllChapters();
  const currentIndex = chapters.findIndex((ch) => ch.slug === slug);

  return {
    current: currentIndex + 1,
    total: chapters.length,
  };
}

export function estimateReadingTime(content: string): number {
  const words = content.trim().split(/\s+/).length;
  return Math.ceil(words / 200);
}

export function countWords(content: string): number {
  return content.trim().split(/\s+/).length;
}

export interface DraftStats {
  chapters: number;
  parts: number;
  words: number;
  citationsPending: number;
  verifyMarks: number;
  forecastsResolved: number;
}

// The book's own discipline, applied to itself: the site reports the
// manuscript's live verification state, computed from source at build time.
export function getDraftStats(): DraftStats {
  let words = 0;
  let citationsPending = 0;
  let verifyMarks = 0;
  let chapters = 0;

  for (const chapter of getAllChapters()) {
    const content = fs.readFileSync(resolveProjectFile(chapter.file), 'utf-8');
    words += countWords(content);
    citationsPending += (content.match(/\[NEEDS CITATION/g) || []).length;
    verifyMarks += (content.match(/\[VERIFY/g) || []).length;
    // Front matter reads on the site but does not count as a chapter.
    if (chapter.chapterNumber != null) chapters += 1;
  }

  return {
    chapters,
    parts: bookStructure.parts.length,
    words,
    citationsPending,
    verifyMarks,
    forecastsResolved: 0,
  };
}
