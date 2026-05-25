import pandas as pd
import matplotlib.pyplot as plt


def plot_group_distribution(
    df: pd.DataFrame,
    col: str,
    top_n: int = 10,
    title: str = "",
) -> None:
    """
    Plot a horizontal bar chart showing the distribution of a categorical column.

    Displays the top_n most frequent values with their counts and percentage
    of non-null entries. Useful for identifying representation bias in grouping
    variables such as country, gender, or class label.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the column.
    col : str
        The categorical column to plot.
    top_n : int
        Number of top values to display. Default 10.
    title : str
        Chart title. Defaults to "Distribution of <col>".
    """
    counts = df[col].value_counts().head(top_n)
    total = df[col].notna().sum()
    pcts = (counts / total * 100).round(1)
    labels = [f"{idx}  ({pct}%)" for idx, pct in zip(counts.index, pcts)]

    fig, ax = plt.subplots(figsize=(8, max(3, len(counts) * 0.5)))
    ax.barh(range(len(counts)), counts.values, color="steelblue")
    ax.set_yticks(range(len(counts)))
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel("Count")
    ax.set_ylabel(col)
    ax.set_title(title or f"Distribution of {col}")
    plt.tight_layout()
    plt.show()


def plot_response_skew(
    df: pd.DataFrame,
    col: str,
    title: str = "",
) -> None:
    """
    Plot a histogram of a numeric column with mean, median, and skewness annotated.

    Useful for identifying measurement bias or ceiling/floor effects in response
    variables such as survey scores, ratings, or session lengths.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the column.
    col : str
        The numeric column to plot.
    title : str
        Chart title. Defaults to "Distribution of <col>".
    """
    data = df[col].dropna()
    skewness = data.skew()

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.hist(data, bins=50, color="steelblue", edgecolor="white")
    ax.axvline(data.median(), color="orange", linestyle="--", linewidth=1.5,
               label=f"Median: {data.median():.0f}")
    ax.axvline(data.mean(), color="red", linestyle="--", linewidth=1.5,
               label=f"Mean: {data.mean():.0f}")
    ax.set_xlabel(col)
    ax.set_ylabel("Count")
    ax.set_title(title or f"Distribution of {col}")
    ax.legend()
    ax.text(0.98, 0.95, f"Skewness: {skewness:.2f}",
            transform=ax.transAxes, ha="right", va="top", fontsize=9,
            bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))
    plt.tight_layout()
    plt.show()


def summarize_coverage(
    reference_ids: pd.Series,
    files: dict[str, pd.DataFrame],
    id_col: str = "pid",
) -> None:
    """
    Print a coverage table comparing unique IDs in each file against a reference set.

    Identifies which participants or entities are missing from each data file,
    surfacing coverage bias before analysis proceeds.

    Parameters
    ----------
    reference_ids : pd.Series or array-like
        The reference set of IDs, typically from the demographics or master table.
    files : dict of str -> pd.DataFrame
        Mapping of file label to DataFrame. Each DataFrame must contain id_col.
    id_col : str
        Column name containing participant or entity IDs. Default "pid".
    """
    ref_set = set(reference_ids.dropna())
    ref_n = len(ref_set)

    print(f"Reference population: {ref_n:,} unique IDs\n")
    print(f"{'File':<30} {'Unique IDs':>12} {'In Reference':>14} {'Coverage':>10}")
    print("-" * 70)

    for label, df in files.items():
        unique_ids = set(df[id_col].dropna().unique())
        in_ref = len(unique_ids & ref_set)
        pct = in_ref / ref_n * 100
        print(f"{label:<30} {len(unique_ids):>12,} {in_ref:>14,} {pct:>9.1f}%")
