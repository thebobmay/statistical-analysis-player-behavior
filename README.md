# Statistical Analysis of Player Behavior and Motivation in Gameplay Telemetry

Udacity AI Masters Capstone - Project 2: Statistical Analysis

**Student:** Robert Mayfield

---

## Project Description

This project conducts a statistical analysis of gameplay telemetry and player motivation data collected from PowerWash Simulator. The analysis examines whether players who report higher intrinsic motivation (enjoyment) tend to play in longer sessions, using descriptive statistics, hypothesis testing, and supplemental predictive modeling.

The workflow covers dataset loading and inspection, data preparation using the Initial Data Analysis framework, descriptive statistics, visualizations, a Mann-Whitney U hypothesis test, and a supplemental baseline vs. experimental model comparison.

---

## Dataset

**Name:** An intensive longitudinal dataset of in-game player behaviour and well-being in PowerWash Simulator
**Source:** Vuorre, M., Magnusson, K., Johannes, N., Butlin, J., & Przybylski, A. K. (2023). Scientific Data, 10, 622.
**License:** CC0 1.0 Universal (public domain)
**Players:** 11,080 across 39 countries over 222 days
**Target variable:** High vs. low enjoyment group (median split of per-player mean Enjoyment score)

See `dataset_access_instructions.md` for full download instructions.

---

## Files Included

```
notebooks/analysis.ipynb                         main project notebook
reports/Statistical_Analysis_Report.pdf          full written analysis report
reports/module_summary.pdf                       identical copy of report
requirements.txt                                 Python dependencies
dataset_access_instructions.md                   dataset source and download steps
data/sample/                                     small sample for quick review
outputs/figures/                                 saved chart files
outputs/tables/                                  summary tables
```

---

## How to Run

1. Create and activate a Python environment (Python 3.13.3 was used for this project):
   ```
   python -m venv .venv
   ```
   On Windows:
   ```
   .venv\Scripts\activate
   ```
   On macOS or Linux:
   ```
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Download the dataset from OSF (see `dataset_access_instructions.md`) and place `data.zip` into `data/raw/`. The notebook reads CSV files directly from the zip archive.
4. Open the notebook in Jupyter:
   ```
   jupyter notebook notebooks/analysis.ipynb
   ```
5. Run all cells from top to bottom.

---

## Bias and Responsible Data Handling

The dataset reflects players who opted into a research study while playing a specific commercial game on Steam, which skews toward engaged players and English-speaking PC gaming demographics. Survey responses are voluntary and may reflect self-selection bias. Enjoyment scores show a strong positive skew, with most players reporting high enjoyment. Results should be interpreted as descriptive of this study population and not generalized to all players or game genres.

---

## Future Integration Reflection

### How this analysis could support the AI Game Director Studio

Statistical patterns in session length and intrinsic motivation establish a quantitative baseline for how engagement signals relate to player behavior. This layer informs how the Game Director might weight or interpret telemetry signals when making recommendations.

### How this dataset and model would need to evolve for deeper integration

The dataset was collected from a single game under research conditions. A production system would need telemetry from multiple titles, real-time collection pipelines, and motivation proxies derived from behavioral signals rather than survey responses, which are unavailable outside a research setting.

### How agentic automation could assist this workflow

An agentic pipeline could monitor live session telemetry, compute rolling engagement metrics per player, flag sessions showing declining motivation proxies, and surface those signals to the Game Director without requiring manual statistical analysis for each new data batch.

---

## Requirements

See `requirements.txt` for the dependency list.

Key libraries: Python 3.13.3, pandas, numpy, scipy, scikit-learn, matplotlib, seaborn, jupyter
