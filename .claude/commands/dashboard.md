---
description: Show book progress dashboard with word counts, citations, and chapter status
---

Run the book dashboard script to show current progress:

```bash
python scripts/book_dashboard.py
```

Then summarize the key findings for the user, including:
1. Overall word count progress (target: 80,000 words)
2. Chapters completed vs remaining
3. Citation coverage
4. Any chapters below target word count (~6,000 words each)
5. Research notes that haven't been linked from chapters

Also remind the user that the interactive HTML dashboard has been generated at `dashboard.html` which they can open in a browser to see the chapter-notes connection graph.
