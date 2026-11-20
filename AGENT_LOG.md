# Agent log

Add a dated entry each time you work with your AI coding agent, with the newest entry at the bottom. Each entry records what you asked the agent, what it produced, and what you checked or changed. Paste your key prompts in exactly as you typed them. Include at least one time the agent got something wrong, and how you caught it.

Copy this outline for each entry:

```markdown
## YYYY-MM-DD: What you worked on

- **Asked:** "Paste your prompt here."
- **Agent produced:** What it made or changed.
- **Checked or changed:** How you checked it, and what you fixed.
```

## 2026-11-20 — College-town median sale prices

- **Asked:**

  > Use the YUELI0410/college-town-home-sales repository. Switch to the existing part1-late branch before editing. If you cannot access that branch, stop and tell me.\
  > \
  > Read AGENTS.md and docs/data_description_sheet.md first. Then replace the placeholder index.html with a simple English webpage comparing median home sale prices across college towns. Use data/college_town_home_sales.csv. Exclude sales below $10,000 and explain this filter on the page.\
  > \
  > Show a table with city, state, number of included sales, and median sale price rounded to the nearest dollar. Sort the table from highest to lowest median price. Keep the dataset citation on the page and leave the original data files unchanged.\
  > \
  > Verify the results for Champaign and Urbana against the CSV. Record the work in AGENT_LOG.md and show me the changes for review. Do not push, merge into main, or deploy yet.

- **Agent produced:** An English webpage with 18 cities ranked by median home sale price, an explanation of the $10,000 cutoff, and the original dataset citation. Added a script that refreshes the table from the CSV and documented it in the README.
- **Checked or changed:** The initial branch switch failed because the checkout lacked a local branch reference. The agent confirmed the branch existed on GitHub, fetched it, and switched to it before editing. An independent SQL calculation loaded the CSV and matched every table row in order. Champaign had 2,285 included sales and a $240,000 median, with one sale excluded. Urbana had 1,131 included sales and a $229,900 median, with zero sales excluded. The refresh script reproduced the page exactly, and Git confirmed that the original data files were unchanged. The page was also checked in Chromium through a localhost preview.
