# Rubric Alignment Checklist
# Statistical Analysis of Player Behavior and Motivation in Gameplay Telemetry
# Udacity AI Masters Capstone — Project 2

**Student:** Robert Mayfield

---

## Pre-Submission Quick Checks

- [x] Uses real non-synthetic public dataset (not from Projects 1 or 2)
- [x] `notebooks/analysis.ipynb` runs top-to-bottom without errors; all cells execute; required outputs visible
- [x] `reports/Statistical_Analysis_Report.pdf` included
- [x] `reports/module_summary.pdf` included (identical copy)
- [x] `requirements.txt` included (generated with pip freeze)
- [x] `dataset_access_instructions.md` included
- [x] `data/sample/` populated with representative sample CSV
- [x] `Rubric_Alignment_Checklist.md` included
- [x] Git history has multiple commits across feature branches and main

---

## Full Rubric

### Technical Implementation

| Criteria | Requirement | Status | Where |
|---|---|---|---|
| Notebook Execution | Runs top-to-bottom without errors; all cells execute; required outputs visible | Pass | `notebooks/analysis.ipynb` |
| Data Preparation and Preprocessing | Dataset loads correctly; appropriate preprocessing applied; choices consistent with analysis | Pass | Sections 2–3: IDA-compliant cleaning, median split, per-player aggregation |
| Statistical Test / Model Implementation | At least one statistical test or ML model correctly implemented; choice appropriate for problem | Pass | Section 6: Mann-Whitney U (scipy.stats); Sections 8.4–8.5: LR and RF via scikit-learn |
| Training and Evaluation | Model trained successfully; evaluated with at least one appropriate metric; results clearly displayed | Pass | Sections 8.4–8.6: accuracy, macro F1, classification report; model_comparison.csv saved |
| Reproducibility | Valid `requirements.txt` generated with `pip freeze` included | Pass | `requirements.txt` pinned from active environment |

### Analytical Reasoning (assessed via module_summary.pdf)

| Criteria | Requirement | Status | Where |
|---|---|---|---|
| Evaluation Metrics Justification | Explains why chosen metrics are appropriate for the model type, task, and dataset | Pass | Report: Evaluation Metrics Justification section; Mann-Whitney U chosen for right-skewed data; macro F1 chosen for balanced classes |
| Results Interpretation | Interprets performance using actual results; explains what metrics indicate about model behavior | Pass | Report: Results and Visual Findings sections; notebook Sections 6–7 |
| Model Limitations and Tradeoffs | Identifies at least one limitation or tradeoff and its impact | Pass | Report: Limitations and Potential Bias section (6 subsections); notebook Section 7.2 |
| Experimental Design Justification | Explains what was changed between baseline and experimental model and why the comparison was meaningful | Pass | Report: Supplemental Classification section — LR as baseline (linear threshold), RF as experimental (non-linear ensemble); Pedregosa et al., 2011 |
| Performance Evaluation and Comparison | Compares results from both models using appropriate metrics; clearly explains observed trade-offs | Pass | Report: Supplemental Classification results table + trade-off sentence (RF feature importance vs. LR output) |

### Ethical and Responsible Practice (assessed via module_summary.pdf)

| Criteria | Requirement | Status | Where |
|---|---|---|---|
| Bias and Responsible Use | Identifies at least one potential source of bias or ethical concern; describes one step taken or proposed to reduce that risk | Pass | Report: Limitations (self-selection bias, ceiling effect, geographic skew); Responsible Use section; notebook Section 8.7 |

### Communication and Presentation (assessed via module_summary.pdf)

| Criteria | Requirement | Status | Where |
|---|---|---|---|
| Notebook Organization | Clear markdown headings; logical structure across data prep, analysis, evaluation, outputs | Pass | Sections 1–9 with subsections; IDA framework followed |
| Code Readability and Documentation | Student code is readable, organized, with docstrings where appropriate | Pass | All student-defined functions have docstrings in `src/inspection.py` and `src/bias.py` |
| Written Analysis Quality | Clearly written, logically structured, understandable to technical and non-technical readers | Pass | Report includes non-technical interpretation section; no undefined jargon |
| Use of Citations | In-text citations when referencing statistical concepts and evaluation methods; References section in consistent style | Pass | APA format; all in-text citations have matching References entries (Cohen 1988, Deci & Ryan 2000, Field 2013, Lusa et al. 2024, Pedregosa et al. 2011, Vuorre et al. 2023) |

### Integration and Professional Relevance

| Criteria | Requirement | Status | Where |
|---|---|---|---|
| Workflow Completeness and Portfolio Readiness | Complete, professional statistical and ML workflow appropriate for a portfolio | Pass | IDA framework, hypothesis testing, supplemental ML comparison, saved outputs, report, Future Integration Reflection section |

---

## Key Analytical Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Dataset | Vuorre et al. (2023) PowerWash Simulator longitudinal dataset | Real, CC0-licensed, contains matched telemetry and validated SDT survey data |
| Survey construct | Enjoyment only | Most direct SDT intrinsic motivation construct; simpler and more interpretable than composite |
| Group assignment | Median split of per-player mean enjoyment score | Standard for skewed continuous variables when group comparison is the goal |
| Outcome variable | Per-player median session length | Robust to right-skewed session distribution; reduces outlier influence |
| Outlier cap | 480 minutes (8 hours) | Reasonable upper bound for continuous play; values above are almost certainly idle sessions |
| Hypothesis test | Mann-Whitney U (two-sided) | Non-parametric; appropriate for right-skewed session length distribution |
| Effect size | Rank-biserial correlation r | Scale-independent; appropriate complement to p-value at large sample sizes |
| Baseline model | Logistic Regression with StandardScaler | Linear classifier with consistent L2 regularization; interpretable threshold |
| Experimental model | Random Forest (100 trees) | Non-linear ensemble; adds feature importance output for production feature selection |
| Classification metrics | Accuracy and macro F1 | Appropriate for balanced binary problem (4,163 vs. 4,176 in modeling dataset) |
