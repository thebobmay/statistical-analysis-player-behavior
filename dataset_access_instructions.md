# Dataset Access Instructions

**Dataset:** An intensive longitudinal dataset of in-game player behaviour and well-being in PowerWash Simulator

**Source:** Vuorre, M., Magnusson, K., Johannes, N., Butlin, J., & Przybylski, A. K. (2023). An intensive longitudinal dataset of in-game player behaviour and well-being in PowerWash Simulator. *Scientific Data, 10*, 622. https://doi.org/10.1038/s41597-023-02530-3

**Data DOI:** https://doi.org/10.17605/OSF.IO/WPEH6

---

## Download Instructions

1. Go to https://osf.io/wpeh6
2. Download the full dataset archive (data.zip)
3. Place `data.zip` (do not extract it) into `data/raw/`

The notebook reads CSV files directly from the zip archive.

---

## Files Used in This Analysis

| File | Contents |
|---|---|
| `study_prompt_answered.csv` | In-game survey responses across all 6 prompt types |
| `exited_game.csv` | Session exit events including session duration |
| `demographics.csv` | Participant-level demographic and summary data |
| `player_logged_in.csv` | Login events per player |
| `job_completed.csv` | Job completion events |

## Files Not Used

The following files are excluded due to size or scope:

| File | Reason |
|---|---|
| `game_saved.csv` | Removed in dataset v1.1.0 |
| `subtask_completed.csv` | 3.7 GB, granularity not needed |
| `update_current_state.csv` | 3.0 GB, granularity not needed |

---

## License

CC0 1.0 Universal (public domain dedication). No restrictions on use.
