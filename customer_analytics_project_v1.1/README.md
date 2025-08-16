# Customer Analytics — Advanced Version

An enhanced version of the original Customer Analytics project, now with **SQLite3** integration and basic-middle level **statistical analysis**.

## Directory Guide (What each folder is for)
- **data/** — Source datasets and the main SQLite database (`german_data.db`). Keep raw files here.
- **notebooks/** — Jupyter notebooks for quick **EDA**, cleaning, and ad-hoc experiments.
- **stats/** — Reusable **statistical analysis** modules (descriptives, correlation, hypothesis tests) and pipeline entry points.
- **visuals/** — Plotting utilities to generate figures used in reports/dashboards.
- **reports/** — Human-readable outputs: summaries, findings, and final notes.

> Tip: If you’re looking for where data is read from, start in **data/**;  
> for modeling/tests, open **stats/**; for charts, check **visuals/**; and for quick exploration, use **notebooks/**.

## Quick Start
```bash
# 1) Install dependencies
pip install -r requirements.txt

# 2) Run the analysis pipeline
python stats/generate_stats.py
Data Source
The project uses SQLite3 (data/german_data.db) as the primary data store.

Requirements

Packages listed in requirements.txt