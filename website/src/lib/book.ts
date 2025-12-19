// Book structure and chapter loading utilities

export interface Chapter {
  slug: string;
  title: string;
  file: string;
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

// Define the book structure based on myst.yml
export const bookStructure: BookStructure = {
  title: "Society in Silico",
  subtitle: "The Story of Policy Simulation",
  author: "Max Ghenis",
  frontMatter: [
    {
      slug: "thesis",
      title: "Thesis",
      file: "manuscript/front-matter/00-thesis.md",
    },
    {
      slug: "preface",
      title: "Preface",
      file: "manuscript/front-matter/00-preface.md",
    },
    {
      slug: "introduction",
      title: "Introduction",
      file: "manuscript/front-matter/01-introduction.md",
    },
  ],
  parts: [
    {
      title: "Origins",
      number: 1,
      chapters: [
        {
          slug: "birth-of-microsimulation",
          title: "The Birth of Microsimulation",
          file: "manuscript/part-1-origins/01-birth-of-microsimulation.md",
          part: "Origins",
          partNumber: 1,
          chapterNumber: 1,
        },
        {
          slug: "tax-model-wars",
          title: "The Tax Model Wars",
          file: "manuscript/part-1-origins/02-tax-model-wars.md",
          part: "Origins",
          partNumber: 1,
          chapterNumber: 2,
        },
        {
          slug: "open-source-revolution",
          title: "The Open Source Revolution",
          file: "manuscript/part-1-origins/03-open-source-revolution.md",
          part: "Origins",
          partNumber: 1,
          chapterNumber: 3,
        },
        {
          slug: "the-accuracy-question",
          title: "The Accuracy Question",
          file: "manuscript/part-1-origins/04-the-accuracy-question.md",
          part: "Origins",
          partNumber: 1,
          chapterNumber: 4,
        },
      ],
    },
    {
      title: "Building",
      number: 2,
      chapters: [
        {
          slug: "policyengine-proof-of-concept",
          title: "PolicyEngine: Proof of Concept",
          file: "manuscript/part-2-building/04-policyengine-proof-of-concept.md",
          part: "Building",
          partNumber: 2,
          chapterNumber: 5,
        },
        {
          slug: "the-household-view",
          title: "The Household View",
          file: "manuscript/part-2-building/05-the-household-view.md",
          part: "Building",
          partNumber: 2,
          chapterNumber: 6,
        },
        {
          slug: "the-society-view",
          title: "The Society View",
          file: "manuscript/part-2-building/06-the-society-view.md",
          part: "Building",
          partNumber: 2,
          chapterNumber: 7,
        },
        {
          slug: "ai-enters-the-picture",
          title: "AI Enters the Picture",
          file: "manuscript/part-2-building/07-ai-enters-the-picture.md",
          part: "Building",
          partNumber: 2,
          chapterNumber: 8,
        },
        {
          slug: "cosilico-infrastructure-for-the-future",
          title: "Cosilico: Infrastructure for the Future",
          file: "manuscript/part-2-building/08-cosilico-infrastructure-for-the-future.md",
          part: "Building",
          partNumber: 2,
          chapterNumber: 9,
        },
      ],
    },
    {
      title: "Future",
      number: 3,
      chapters: [
        {
          slug: "the-uncertainty-gap",
          title: "The Uncertainty Gap",
          file: "manuscript/part-3-future/10-the-uncertainty-gap.md",
          part: "Future",
          partNumber: 3,
          chapterNumber: 10,
        },
        {
          slug: "simulating-opinion",
          title: "Simulating Opinion",
          file: "manuscript/part-3-future/11-simulating-opinion.md",
          part: "Future",
          partNumber: 3,
          chapterNumber: 11,
        },
        {
          slug: "simulating-democracy",
          title: "Simulating Democracy",
          file: "manuscript/part-3-future/12-simulating-democracy.md",
          part: "Future",
          partNumber: 3,
          chapterNumber: 12,
        },
        {
          slug: "simulating-values",
          title: "Simulating Values",
          file: "manuscript/part-3-future/13-simulating-values.md",
          part: "Future",
          partNumber: 3,
          chapterNumber: 13,
        },
        {
          slug: "society-in-silico",
          title: "Society in Silico",
          file: "manuscript/part-3-future/14-society-in-silico.md",
          part: "Future",
          partNumber: 3,
          chapterNumber: 14,
        },
      ],
    },
  ],
};

// Get all chapters in reading order
export function getAllChapters(): Chapter[] {
  const chapters: Chapter[] = [...bookStructure.frontMatter];
  for (const part of bookStructure.parts) {
    chapters.push(...part.chapters);
  }
  return chapters;
}

// Get chapter by slug
export function getChapterBySlug(slug: string): Chapter | undefined {
  return getAllChapters().find((chapter) => chapter.slug === slug);
}

// Get previous and next chapters for navigation
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

// Get chapter position (e.g., "Chapter 3 of 14")
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

// Estimate reading time (average 200 words per minute)
export function estimateReadingTime(content: string): number {
  const words = content.trim().split(/\s+/).length;
  return Math.ceil(words / 200);
}

// Count words in content
export function countWords(content: string): number {
  return content.trim().split(/\s+/).length;
}
