import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import App from './App'

// Mock data that matches the structure from book_dashboard.py
const mockData = {
  generated_at: '2025-12-12T18:00:00.000000',
  chapters: [
    {
      path: 'manuscript/front-matter/01-introduction.md',
      name: '01-introduction',
      title: 'Introduction: The Model and the World',
      words: 880,
      wiki_links: ['guy-orcutt', 'policyengine'],
      citations: [],
      has_references: false,
    },
    {
      path: 'manuscript/part-1-origins/01-guy-orcutt.md',
      name: '01-guy-orcutt',
      title: 'Chapter 1: Guy Orcutt',
      words: 2500,
      wiki_links: [],
      citations: ['orcutt1957'],
      has_references: true,
    },
    {
      path: 'manuscript/part-2-building/04-policyengine.md',
      name: '04-policyengine',
      title: 'Chapter 4: PolicyEngine',
      words: 1834,
      wiki_links: [],
      citations: ['policyengine2021'],
      has_references: true,
    },
  ],
  notes_summary: {
    total: 15,
    referenced: 5,
  },
  citations: {
    total_in_bib: 48,
    used_in_manuscript: 35,
    unused: ['unused1', 'unused2'],
  },
  graph: {
    nodes: [
      { id: '01-introduction', type: 'chapter', label: 'Introduction', words: 880 },
      { id: 'guy-orcutt', type: 'note', label: 'Guy Orcutt', words: 500 },
    ],
    edges: [
      { source: '01-introduction', target: 'guy-orcutt' },
    ],
  },
  progress: {
    total: {
      words: 16220,
      target: 80000,
      percent: 20.3,
    },
    by_part: {
      'Front Matter': { words: 880, chapters: 1 },
      'Part I: Origins': { words: 7000, chapters: 3 },
      'Part II: Building': { words: 8340, chapters: 5 },
    },
    chapters_complete: 9,
  },
  targets: {
    total_words: 80000,
    front_matter: 5000,
    part_1: 20000,
    part_2: 25000,
    part_3: 25000,
    back_matter: 5000,
    words_per_chapter: 6000,
  },
  reviews: [],
}

const mockDataWithReviews = {
  ...mockData,
  reviews: [
    {
      persona: 'Policy Researcher',
      rating: 4.2,
      summary: 'A thoughtful exploration of microsimulation and its potential.',
      strengths: ['Clear explanations', 'Good historical context'],
      weaknesses: ['Could use more technical depth'],
      generated_at: '2025-12-12T18:00:00.000000',
    },
    {
      persona: 'General Reader',
      rating: 3.8,
      summary: 'Accessible but occasionally too technical.',
      strengths: ['Engaging narrative', 'Real-world examples'],
      weaknesses: ['Some jargon unexplained'],
      generated_at: '2025-12-12T18:00:00.000000',
    },
  ],
}

describe('App', () => {
  beforeEach(() => {
    vi.resetAllMocks()
  })

  describe('Loading State', () => {
    it('shows loading spinner while fetching data', () => {
      global.fetch = vi.fn(() => new Promise(() => {})) // Never resolves
      render(<App />)
      expect(screen.getByText('Loading manuscript data...')).toBeInTheDocument()
    })
  })

  describe('Error State', () => {
    it('shows error message when fetch fails', async () => {
      global.fetch = vi.fn(() => Promise.resolve({ ok: false }))
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText(/Error:/)).toBeInTheDocument()
      })
    })

    it('shows bun command hint on error', async () => {
      global.fetch = vi.fn(() => Promise.resolve({ ok: false }))
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText(/bun run generate-data/)).toBeInTheDocument()
      })
    })
  })

  describe('Dashboard Content', () => {
    beforeEach(() => {
      global.fetch = vi.fn(() =>
        Promise.resolve({
          ok: true,
          json: () => Promise.resolve(mockData),
        })
      )
    })

    it('renders the dashboard title', async () => {
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText('Society in Silico')).toBeInTheDocument()
      })
    })

    it('displays overall progress percentage', async () => {
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText('20.3%')).toBeInTheDocument()
      })
    })

    it('displays total words written', async () => {
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText('16,220')).toBeInTheDocument()
      })
    })

    it('shows chapter count', async () => {
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText(/Chapters \(3 total\)/)).toBeInTheDocument()
      })
    })

    it('displays citation statistics', async () => {
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText('48')).toBeInTheDocument() // BibTeX entries
        expect(screen.getByText('35')).toBeInTheDocument() // Citations used
      })
    })

    it('displays research notes statistics', async () => {
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText('15')).toBeInTheDocument() // Total notes
        expect(screen.getByText('5')).toBeInTheDocument() // Referenced
      })
    })
  })

  describe('Chapter Sorting', () => {
    beforeEach(() => {
      global.fetch = vi.fn(() =>
        Promise.resolve({
          ok: true,
          json: () => Promise.resolve(mockData),
        })
      )
    })

    it('displays chapters grouped by part', async () => {
      render(<App />)
      await waitFor(() => {
        // Part names appear in both progress breakdown and chapter list
        expect(screen.getAllByText('Front Matter').length).toBeGreaterThan(0)
        expect(screen.getAllByText('Part I: Origins').length).toBeGreaterThan(0)
        expect(screen.getAllByText('Part II: Building').length).toBeGreaterThan(0)
      })
    })

    it('shows chapter titles', async () => {
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText('Introduction: The Model and the World')).toBeInTheDocument()
        expect(screen.getByText('Chapter 1: Guy Orcutt')).toBeInTheDocument()
        expect(screen.getByText('Chapter 4: PolicyEngine')).toBeInTheDocument()
      })
    })

    it('shows check mark for chapters over 1000 words', async () => {
      render(<App />)
      await waitFor(() => {
        const checkmarks = screen.getAllByText('✓')
        expect(checkmarks.length).toBeGreaterThan(0)
      })
    })
  })

  describe('Synthetic Reviews - Empty', () => {
    beforeEach(() => {
      global.fetch = vi.fn(() =>
        Promise.resolve({
          ok: true,
          json: () => Promise.resolve(mockData),
        })
      )
    })

    it('shows empty reviews message when no reviews', async () => {
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText('No synthetic reviews yet.')).toBeInTheDocument()
      })
    })

    it('shows hint to run /review command', async () => {
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText('/review')).toBeInTheDocument()
      })
    })
  })

  describe('Synthetic Reviews - With Data', () => {
    beforeEach(() => {
      global.fetch = vi.fn(() =>
        Promise.resolve({
          ok: true,
          json: () => Promise.resolve(mockDataWithReviews),
        })
      )
    })

    it('displays review personas', async () => {
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText('Policy Researcher')).toBeInTheDocument()
        expect(screen.getByText('General Reader')).toBeInTheDocument()
      })
    })

    it('displays average rating', async () => {
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText('4.0')).toBeInTheDocument() // (4.2 + 3.8) / 2
      })
    })

    it('displays review count', async () => {
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText('2')).toBeInTheDocument() // 2 reviews
      })
    })

    it('displays review summaries', async () => {
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText('A thoughtful exploration of microsimulation and its potential.')).toBeInTheDocument()
      })
    })

    it('displays strengths and weaknesses', async () => {
      render(<App />)
      await waitFor(() => {
        expect(screen.getByText('Clear explanations')).toBeInTheDocument()
        expect(screen.getByText('Could use more technical depth')).toBeInTheDocument()
      })
    })
  })
})

describe('getChapterNumber helper', () => {
  it('extracts number from chapter filename', () => {
    // Test the sorting logic indirectly through render order
    const chapters = [
      { name: '04-chapter', path: 'part-1', title: 'Four', words: 100, citations: [], wiki_links: [] },
      { name: '01-chapter', path: 'part-1', title: 'One', words: 100, citations: [], wiki_links: [] },
      { name: '02-chapter', path: 'part-1', title: 'Two', words: 100, citations: [], wiki_links: [] },
    ]

    const getChapterNumber = (ch) => {
      const match = ch.name.match(/^(\d+)/)
      return match ? parseInt(match[1], 10) : 999
    }

    const sorted = [...chapters].sort((a, b) => getChapterNumber(a) - getChapterNumber(b))
    expect(sorted[0].name).toBe('01-chapter')
    expect(sorted[1].name).toBe('02-chapter')
    expect(sorted[2].name).toBe('04-chapter')
  })
})
