import React, { useState, useEffect, useRef } from 'react'
import * as d3 from 'd3'

function App() {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const graphRef = useRef(null)

  useEffect(() => {
    fetch('./data.json')
      .then(res => {
        if (!res.ok) throw new Error('Failed to load data')
        return res.json()
      })
      .then(setData)
      .catch(err => setError(err.message))
      .finally(() => setLoading(false))
  }, [])

  useEffect(() => {
    if (data && graphRef.current) {
      renderGraph(data.graph, graphRef.current)
    }
  }, [data])

  if (loading) {
    return (
      <div className="loading">
        <div className="loading-spinner" />
        <div className="loading-text">Loading manuscript data...</div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="loading">
        <div className="loading-text">
          Error: {error}
          <br />
          <small>Run: npm run generate-data</small>
        </div>
      </div>
    )
  }

  const { progress, chapters, citations, notes_summary, targets, generated_at } = data
  const formattedDate = new Date(generated_at).toLocaleDateString('en-US', {
    month: 'long',
    day: 'numeric',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })

  // Group chapters by part
  const chaptersByPart = chapters.reduce((acc, ch) => {
    let part = 'Other'
    if (ch.path.includes('part-1')) part = 'Part I: Origins'
    else if (ch.path.includes('part-2')) part = 'Part II: Building'
    else if (ch.path.includes('part-3')) part = 'Part III: Future'
    else if (ch.path.includes('front-matter')) part = 'Front Matter'

    if (!acc[part]) acc[part] = []
    acc[part].push(ch)
    return acc
  }, {})

  return (
    <div className="dashboard">
      {/* Header */}
      <header className="header fade-up">
        <div className="header-title">
          <h1>Society in Silico</h1>
          <h2>Book Progress Dashboard</h2>
        </div>
        <div className="header-meta">
          <span>Generated: {formattedDate}</span>
          <span>Target: {targets.total_words.toLocaleString()} words</span>
        </div>
      </header>

      {/* Progress Hero */}
      <section className="progress-section fade-up delay-1">
        <div className="progress-hero">
          <div className="progress-bar-container">
            <div className="progress-bar">
              <div
                className="progress-fill"
                style={{ width: `${progress.total.percent}%` }}
              />
            </div>
            <div className="progress-labels">
              <span>0</span>
              <span>{Math.floor(targets.total_words / 4).toLocaleString()}</span>
              <span>{Math.floor(targets.total_words / 2).toLocaleString()}</span>
              <span>{Math.floor(targets.total_words * 3 / 4).toLocaleString()}</span>
              <span>{targets.total_words.toLocaleString()}</span>
            </div>
          </div>
          <div className="progress-stats">
            <div className="stat-large">
              <div className="value">{progress.total.percent}%</div>
              <div className="label">Complete</div>
            </div>
            <div className="stat-large">
              <div className="value">{progress.total.words.toLocaleString()}</div>
              <div className="label">Words Written</div>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Grid */}
      <div className="grid">
        {/* Parts Breakdown */}
        <div className="card grid-span-8 fade-up delay-2">
          <h3>Progress by Part</h3>
          <div className="parts-breakdown">
            {Object.entries(progress.by_part).map(([part, stats]) => {
              const target = part.includes('Part I') ? targets.part_1
                : part.includes('Part II') ? targets.part_2
                : part.includes('Part III') ? targets.part_3
                : part.includes('Front') ? targets.front_matter
                : targets.back_matter
              const percent = Math.min(100, Math.round(100 * stats.words / target))

              return (
                <div className="part-row" key={part}>
                  <span className="part-name">{part}</span>
                  <div className="part-bar">
                    <div
                      className="part-bar-fill"
                      style={{ width: `${percent}%` }}
                    />
                  </div>
                  <span className="part-count">
                    {stats.words.toLocaleString()} / {target.toLocaleString()}
                  </span>
                </div>
              )
            })}
          </div>
        </div>

        {/* Citations & Research */}
        <div className="card grid-span-4 fade-up delay-3">
          <h3>Research & Citations</h3>
          <div className="stats-grid">
            <div className="stat-item">
              <div className="value">{citations.total_in_bib}</div>
              <div className="label">BibTeX Entries</div>
            </div>
            <div className="stat-item">
              <div className="value">{citations.used_in_manuscript}</div>
              <div className="label">Citations Used</div>
            </div>
            <div className="stat-item">
              <div className="value">{notes_summary.total}</div>
              <div className="label">Research Notes</div>
            </div>
            <div className="stat-item">
              <div className="value">{notes_summary.referenced}</div>
              <div className="label">Notes Referenced</div>
            </div>
          </div>
        </div>

        {/* Chapters List */}
        <div className="card grid-span-6 fade-up delay-4">
          <h3>Chapters ({chapters.length} total)</h3>
          <div className="chapter-list">
            {Object.entries(chaptersByPart).map(([part, partChapters]) => (
              <React.Fragment key={part}>
                {partChapters.map((ch, idx) => (
                  <div className="chapter-item" key={ch.name}>
                    <div className="chapter-status">
                      {ch.words > 1000 ? '✓' : '◯'}
                    </div>
                    <div className="chapter-info">
                      <div className="chapter-title">{ch.title}</div>
                      <div className="chapter-part">{part}</div>
                    </div>
                    <div className="chapter-stats">
                      <span className="chapter-stat words">
                        {ch.words.toLocaleString()} words
                      </span>
                      <span className="chapter-stat">
                        {ch.citations.length} cites
                      </span>
                      <span className="chapter-stat">
                        {ch.wiki_links.length} links
                      </span>
                      <div className="mini-progress">
                        <div
                          className="mini-progress-fill"
                          style={{
                            width: `${Math.min(100, Math.round(100 * ch.words / targets.words_per_chapter))}%`
                          }}
                        />
                      </div>
                    </div>
                  </div>
                ))}
              </React.Fragment>
            ))}
          </div>
        </div>

        {/* Graph */}
        <div className="card grid-span-6 fade-up delay-5">
          <h3>Chapter ↔ Research Notes Graph</h3>
          <div className="graph-container" ref={graphRef} />
          <div className="legend">
            <div className="legend-item">
              <div className="legend-dot chapter" />
              <span>Chapter</span>
            </div>
            <div className="legend-item">
              <div className="legend-dot note" />
              <span>Research Note</span>
            </div>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="footer fade-up delay-6">
        <span>Society in Silico — Max Ghenis</span>
        <span>
          Refresh: <a href="#" onClick={(e) => { e.preventDefault(); window.location.reload() }}>↻</a>
        </span>
      </footer>
    </div>
  )
}

function renderGraph(graphData, container) {
  // Clear existing
  d3.select(container).selectAll('*').remove()

  if (!graphData.nodes.length) {
    d3.select(container)
      .append('div')
      .style('display', 'flex')
      .style('align-items', 'center')
      .style('justify-content', 'center')
      .style('height', '100%')
      .style('color', 'var(--amber-dim)')
      .style('font-style', 'italic')
      .text('No connections yet...')
    return
  }

  const width = container.clientWidth
  const height = 500

  const svg = d3.select(container)
    .append('svg')
    .attr('width', width)
    .attr('height', height)
    .attr('viewBox', [0, 0, width, height])

  // Create simulation
  const simulation = d3.forceSimulation(graphData.nodes)
    .force('link', d3.forceLink(graphData.edges)
      .id(d => d.id)
      .distance(80))
    .force('charge', d3.forceManyBody().strength(-300))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collision', d3.forceCollide().radius(30))

  // Add links
  const link = svg.append('g')
    .selectAll('line')
    .data(graphData.edges)
    .join('line')
    .attr('class', 'link')
    .attr('stroke-width', 1.5)

  // Add nodes
  const node = svg.append('g')
    .selectAll('g')
    .data(graphData.nodes)
    .join('g')
    .call(d3.drag()
      .on('start', (event, d) => {
        if (!event.active) simulation.alphaTarget(0.3).restart()
        d.fx = d.x
        d.fy = d.y
      })
      .on('drag', (event, d) => {
        d.fx = event.x
        d.fy = event.y
      })
      .on('end', (event, d) => {
        if (!event.active) simulation.alphaTarget(0)
        d.fx = null
        d.fy = null
      }))

  // Node circles
  node.append('circle')
    .attr('r', d => d.type === 'chapter' ? 14 : 8)
    .attr('class', d => d.type === 'chapter' ? 'node-chapter' : 'node-note')

  // Node labels
  node.append('text')
    .attr('class', 'node-label')
    .attr('dx', d => d.type === 'chapter' ? 18 : 12)
    .attr('dy', 4)
    .text(d => d.label)

  // Tick handler
  simulation.on('tick', () => {
    link
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y)

    node.attr('transform', d => `translate(${d.x},${d.y})`)
  })
}

export default App
