# Statistical Analysis of Player Behavior and Motivation in Gameplay Telemetry

**Student:** Robert Mayfield  
**Course:** Udacity AI Masters Capstone, Project 2: Statistical Analysis

---

## Overview

This project examines whether players who report higher intrinsic enjoyment tend to play in longer sessions, using longitudinal gameplay telemetry and survey data collected from players of PowerWash Simulator. The analysis follows the Initial Data Analysis framework (Lusa et al., 2024), which emphasizes systematic inspection of data structure, quality, and potential bias before any hypothesis is tested. The primary analytical method is a two-sided Mann-Whitney U test comparing per player median session lengths between a High enjoyment group and a Low enjoyment group. A supplemental binary classification comparison using Logistic Regression and Random Forest is included to evaluate whether behavioral telemetry features can predict group membership without access to survey responses.

---

## Dataset Description

The dataset is an intensive longitudinal study of player behavior and well being in PowerWash Simulator, collected and published by Vuorre et al. (2023) under a CC0 1.0 public domain license (https://doi.org/10.17605/OSF.IO/WPEH6). It covers 11,080 participants across 39 countries over 222 days of data collection. Data were collected through a combination of automatic gameplay telemetry events and in game survey prompts delivered at regular intervals during play.

Five files were used in this analysis:


| File                        | Contents                                                                 |
| --------------------------- | ------------------------------------------------------------------------ |
| `demographics.csv`          | One row per participant: age, country, gender, login count               |
| `study_prompt_answered.csv` | 702,209 survey responses across six Self Determination Theory constructs |
| `exited_game.csv`           | 105,869 session exit events including `CurrentSessionLength` in minutes  |
| `player_logged_in.csv`      | 113,004 login events                                                     |
| `job_completed.csv`         | 155,100 job completion events                                            |


Three additional files were excluded: `game_saved.csv` is deprecated in dataset version 1.1.0, and `subtask_completed.csv` and `update_current_state.csv` provide sub session event granularity not required for session-level analysis and would exceed available memory when loaded.

The analysis uses Enjoyment responses exclusively, as Enjoyment is the Self Determination Theory construct most directly associated with intrinsic motivation (Deci & Ryan, 2000).

---

## Methods

### Research Question

Do players who report higher enjoyment tend to play in longer sessions?

### Null and Alternative Hypotheses

**Null hypothesis:** The distribution of median session length is the same in the High and Low enjoyment groups.

**Alternative hypothesis:** The distribution of median session length differs between groups.

**Significance threshold:** α = 0.05

### Group Assignment

Players were assigned to High or Low enjoyment groups using a median split of each player's mean enjoyment score across all their recorded Enjoyment responses. Players at or above the median were assigned to the High group; players below the median were assigned to the Low group. The median split is appropriate when the outcome distribution is skewed and parametric assumptions cannot be met (Lusa et al., 2024).

### Hypothesis Test

A two sided Mann-Whitney U test was used to compare per player median session lengths between groups. The Mann-Whitney U test is a non-parametric rank based test appropriate when the normality assumption cannot be met (Field, 2013). Per player median session length, rather than mean, was used as the outcome variable to reduce the influence of the right skewed session length distribution.

Effect size was reported as the rank-biserial correlation r. Values near 0 indicate no effect; |r| < 0.1 is negligible, 0.1 to 0.3 is small, 0.3 to 0.5 is medium, and above 0.5 is large (Cohen, 1988).

### Visualizations

Three charts were produced to support interpretation of the data and results. A histogram of per player median session lengths illustrates the right-skewed distribution that motivates the choice of a non-parametric test. A side-by-side boxplot compares session length distributions between the High and Low enjoyment groups, making the overlap and small separation between groups visually apparent. A histogram of per player mean enjoyment scores shows the ceiling effect and negative skew that characterize the study population. Each chart includes a Markdown interpretation cell immediately following it in the notebook.

---

## Data Preparation

### Demographics

One hundred twenty participants with age values of 100 or above were removed as implausible data entry errors, leaving 10,960 participants.

### Session Length

The following cleaning steps were applied to `exited_game.csv`:

- 1 duplicate row removed
- 14 rows with null `CurrentSessionLength` removed
- 5,769 rows with zero or negative session lengths removed (instrument artifacts from clock adjustments)
- 1,610 sessions exceeding 480 minutes removed as implausible continuous play (sessions left running unattended)

After cleaning, 98,475 session records remained across 10,690 unique players.

### Survey Filtering and Aggregation

Enjoyment responses were filtered from the full survey file (154,152 out of 702,209 responses). Rows with null response values were excluded (148,732 responses retained). Each player's responses were collapsed to a single mean score, producing 8,481 players with at least one Enjoyment response.

### Analysis Dataset

The final analysis dataset was assembled by inner joining players with both a mean enjoyment score and at least one valid session record, then left joining job completions and login counts. This produced 8,418 players: 4,206 in the High group and 4,212 in the Low group.

---

## Evaluation Metrics Justification

The Mann-Whitney U test was chosen over an independent samples t-test because the distribution of per player median session lengths is strongly right skewed (skewness 2.06), violating the normality assumption required for the t-test. The Mann-Whitney U test compares rank distributions rather than means and is robust to this distributional shape (Field, 2013).

Effect size is reported alongside the p-value because statistical significance alone is insufficient for interpreting results with large samples. With over 4,200 players per group, the test has power to detect trivially small differences. The rank-biserial correlation r provides a scale independent measure of the practical magnitude of any detected difference (Cohen, 1988).

For the supplemental classification models, macro F1 and accuracy are reported for a balanced binary classification problem. Both metrics are appropriate because the two groups are nearly equal in size (4,163 vs. 4,176).

---

## Results

### Descriptive Statistics


| Group | Players | Median Enjoyment | Median Session (min) | Median Sessions | Median Job Completions |
| ----- | ------- | ---------------- | -------------------- | --------------- | ---------------------- |
| High  | 4,206   | 959.4            | 67.0                 | 6               | 12                     |
| Low   | 4,212   | 749.0            | 64.2                 | 7               | 12                     |


The enjoyment separation between groups is large (approximately 210 VAS points). The session length difference is small (2.8 minutes). Engagement volume metrics (session count, job completions, logins) are nearly identical between groups.

### Hypothesis Test


| Metric          | Value                  |
| --------------- | ---------------------- |
| Mann-Whitney U  | 9,122,594              |
| P-value         | 0.0176                 |
| Rank-biserial r | 0.03                   |
| Effect size     | Negligible             |
| Decision        | Reject null hypothesis |


The null hypothesis is rejected at α = 0.05. The High enjoyment group tends toward slightly longer sessions, but the effect size of r = 0.03 is negligible.

### Supplemental Classification


| Model               | Accuracy | Macro F1 |
| ------------------- | -------- | -------- |
| Logistic Regression | 0.5186   | 0.51     |
| Random Forest       | 0.5078   | 0.51     |


Both models perform at approximately 51% accuracy, indistinguishable from a random baseline. The Random Forest feature importance ranking places median session length first (0.479), followed by job completions (0.237), login count (0.148), and session count (0.136).

---

## Interpretation for a Non-Technical Audience

The study asked whether players who enjoy a game more tend to play longer each session. The statistical test found a real difference between the groups, but a very small one: the High enjoyment group had a median session length of 67.0 minutes compared to 64.2 minutes for the Low group, a difference of 2.8 minutes. In practical terms, this difference is too small to be meaningful for any design or business decision.

Neither a simple model nor a more complex one could predict which enjoyment group a player belonged to just by looking at their play behavior, performing no better than a coin flip. This tells us that how much a player reports enjoying the game is not strongly connected to how long they play or how many tasks they complete in this dataset.

This does not mean the relationship does not exist. The study population consists almost entirely of players who chose to participate in a research study while playing a game they already liked. Players who disengaged from the game likely dropped out before the study could capture their responses. The comparison is effectively between players who enjoyed the game a great deal and players who enjoyed it very much, not between engaged and disengaged players.

---

## Limitations and Potential Bias

### Self-Selection Bias

Participation required opting into in game surveys during active gameplay. Players with low motivation were less likely to remain enrolled, compressing the lower range of the enjoyment distribution. Both the Low and High enjoyment groups reported high enjoyment (medians of 749 and 959 out of 1000). The analysis compares players at different levels of high enjoyment, not engaged versus disengaged players.

### Ceiling Effect

The enjoyment distribution is negatively skewed (skewness -0.92) with a spike near the maximum of 1000. The median split divides players who reported very high enjoyment from those who reported moderately high enjoyment. A genuine low motivation contrast group is not present in the data.

### Geographic Skew

The United States accounts for 54% of the sample (5,978 of 11,080 participants). Results may not generalize to player populations in other regions.

### Single-Game Scope

All data comes from PowerWash Simulator, a relaxed single player game. Session length dynamics in competitive, narrative, or multiplayer games may respond differently to intrinsic motivation.

### Session Length as a Proxy

`CurrentSessionLength` measures time between game launch and close, not active play intensity. A player who left the game running unattended would produce a longer session record than one who played intensively and quit. The per player median and the 480 minute cap reduce but do not eliminate this noise.

### Median Split Limitations

Dichotomizing a continuous variable discards variation within groups and treats players near the threshold as categorically different when they may be nearly identical. A continuous regression approach would preserve this information but faces the same distributional constraints.

---

## Responsible Use

The data collection design used in this study, pairing behavioral telemetry with timed in game survey prompts, is a legitimate and ethically sound research methodology when participants provide informed consent, as they did in this study. Applying this methodology in a commercial game without disclosure would raise concerns about player autonomy and transparency.

The near chance performance of the classification models (51% accuracy) means any system relying on these models to predict player motivation would be operating near random. Predicted group labels should be treated as probabilistic signals, not ground truth, and should not be used to make irreversible decisions about player experience without human review.

Any production system collecting motivation related telemetry should provide clear disclosure of what data is collected, how inferred states are used, and how players can opt out.

---

## Future Integration Reflection

### How this analysis supports a game intelligence system

This project validates the data collection methodology and identifies the right behavioral features for a player motivation inference system. Session length ranks as the strongest behavioral correlate with self reported enjoyment in the Random Forest feature importance analysis (importance 0.479), followed by job completions, login count, and session count. These are the variables worth instrumenting in any production telemetry pipeline.

The analysis also characterizes the failure mode: the methodology degrades when the player population is homogeneous, so any production system needs data covering the full engagement spectrum, including disengaged players who drop out early.

### How the dataset and methodology would need to evolve

Two pathways would produce a more useful dataset for a production system:

**Active playtester signal collection:** Deploy timed motivation prompts during internal playtesting, where the player pool is intentionally diverse and includes players at all engagement levels. The same analysis pipeline used here applies directly.

**Passive operational inference:** Once the system accumulates live operational data across a broad player base, survey responses can be removed. Behavioral signals alone can be used for motivation inference when the population has sufficient range. The current analysis establishes which features to instrument and what the model would look like.

### How agentic automation could assist this workflow

An agentic pipeline could monitor live session telemetry, compute rolling engagement metrics per player, flag sessions showing declining motivation signals, and surface those signals to a game director without requiring manual statistical analysis for each new data batch. The feature set identified here (session length, job completions, login frequency) provides a starting point for the feature engineering layer of such a pipeline.

---

## References

Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum Associates.

Deci, E. L., & Ryan, R. M. (2000). The "what" and "why" of goal pursuits: Human needs and the self-determination of behavior. *Psychological Inquiry, 11*(4), 227-268. https://doi.org/10.1207/S15327965PLI1104_01

Field, A. (2013). *Discovering statistics using IBM SPSS statistics* (4th ed.). SAGE Publications.

Lusa, L., Proust-Lima, C., Schmidt, C. O., Lee, K. J., le Cessie, S., Baillie, M., Lawrence, F., & Huebner, M., on behalf of TG3 of the STRATOS Initiative. (2024). Initial data analysis for longitudinal studies to build a solid foundation for reproducible analysis. *PLOS ONE, 19*(5), e0295726. https://doi.org/10.1371/journal.pone.0295726

Vuorre, M., Magnusson, K., Johannes, N., Butlin, J., & Przybylski, A. K. (2023). An intensive longitudinal dataset of in-game player behaviour and well-being in PowerWash Simulator. *Scientific Data, 10*, 622. https://doi.org/10.1038/s41597-023-02530-3