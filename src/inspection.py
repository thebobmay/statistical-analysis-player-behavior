import math
import pandas as pd
import matplotlib.pyplot as plt


def inspect_dataframe(df: pd.DataFrame) -> None:
    """
    Print a comprehensive inspection report for any pandas DataFrame.

    Covers shape, data types, memory usage, missing values, duplicate rows,
    numeric and categorical descriptive statistics, unique value counts per
    categorical column, and a head and tail sample.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to inspect.
    """
    sep = "-" * 60

    print("SHAPE AND STRUCTURE")
    print(sep)
    print(f"Rows:    {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]}")
    print()

    print("COLUMN NAMES AND DATA TYPES")
    print(sep)
    print(df.dtypes.to_string())
    print()

    print("MEMORY USAGE")
    print(sep)
    total_mb = df.memory_usage(deep=True).sum() / 1024 ** 2
    print(f"Total: {total_mb:.2f} MB")
    print()

    print("MISSING VALUES")
    print(sep)
    null_counts = df.isnull().sum()
    null_pct = (null_counts / len(df) * 100).round(2)
    missing = pd.DataFrame({"Null Count": null_counts, "Null %": null_pct})
    missing = missing[missing["Null Count"] > 0].sort_values("Null Count", ascending=False)
    if missing.empty:
        print("No missing values found.")
    else:
        print(missing.to_string())
    print()

    print("DUPLICATE ROWS")
    print(sep)
    print(f"Duplicate rows: {df.duplicated().sum():,}")
    print()

    print("DESCRIPTIVE STATISTICS (NUMERIC)")
    print(sep)
    print(df.describe().to_string())
    print()

    categorical_cols = df.select_dtypes(include=["object", "category"]).columns

    if len(categorical_cols) > 0:
        print("DESCRIPTIVE STATISTICS (CATEGORICAL)")
        print(sep)
        print(df[categorical_cols].describe().to_string())
        print()

        print("UNIQUE VALUES PER CATEGORICAL COLUMN")
        print(sep)
        for col in categorical_cols:
            print(f"{col}: {df[col].nunique()} unique values")
        print()

    print("SAMPLE DATA")
    print(sep)
    print("First 5 rows:")
    print(df.head().to_string())
    print()
    print("Last 5 rows:")
    print(df.tail().to_string())


def plot_missing(df: pd.DataFrame, title: str = "Missing Values by Column") -> None:
    """
    Plot a horizontal bar chart of missing value percentages for each column.

    Only columns with at least one missing value are shown. If the DataFrame
    has no missing values, the function prints a message and returns without
    producing a figure.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to examine.
    title : str
        Title displayed on the chart.
    """
    null_pct = (df.isnull().sum() / len(df) * 100).round(2)
    null_pct = null_pct[null_pct > 0].sort_values()

    if null_pct.empty:
        print("No missing values to plot.")
        return

    fig, ax = plt.subplots(figsize=(8, max(3, len(null_pct) * 0.5)))
    ax.barh(null_pct.index, null_pct.values, color="steelblue")
    ax.set_xlabel("Missing (%)")
    ax.set_ylabel("Column")
    ax.set_title(title)
    ax.set_xlim(0, 100)

    for i, (col, val) in enumerate(zip(null_pct.index, null_pct.values)):
        ax.text(val + 0.5, i, f"{val}%", va="center", fontsize=9)

    plt.tight_layout()
    plt.show()


def plot_numeric_distributions(
    df: pd.DataFrame,
    cols: list[str] | None = None,
    title_prefix: str = "",
) -> None:
    """
    Plot histograms for numeric columns in a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    cols : list of str, optional
        Specific numeric columns to plot. Defaults to all numeric columns.
    title_prefix : str
        Optional label prepended to each subplot title (e.g., the file name).
    """
    if cols is None:
        cols = df.select_dtypes(include="number").columns.tolist()

    if not cols:
        print("No numeric columns to plot.")
        return

    n_cols = min(3, len(cols))
    n_rows = math.ceil(len(cols) / n_cols)

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5 * n_cols, 4 * n_rows))
    axes = axes.flatten() if len(cols) > 1 else [axes]

    for i, col in enumerate(cols):
        data = df[col].dropna()
        axes[i].hist(data, bins=40, color="steelblue", edgecolor="white")
        label = f"{title_prefix}: {col}" if title_prefix else col
        axes[i].set_title(label)
        axes[i].set_xlabel(col)
        axes[i].set_ylabel("Count")

    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()
    plt.show()
