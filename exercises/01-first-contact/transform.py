"""
Sales data transformation utilities.

Loads a CSV of sales orders and provides functions to clean,
filter, and summarise the data.
"""

import csv
import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_csv(file_path: Path) -> list[dict]:
    """Load a CSV file and return a list of row dictionaries.

    Args:
        file_path: Path to the CSV file.

    Returns:
        A list of dicts, one per row, with string values.
    """
    rows = []
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(dict(row))
    return rows


# ---------------------------------------------------------------------------
# Data cleaning
# ---------------------------------------------------------------------------

def clean_row(row: dict) -> dict:
    """Convert raw string values in a row to the correct Python types.

    Converts:
        - quantity  -> int
        - unit_price -> float
        - order_date -> datetime.date

    Args:
        row: A raw row dict from load_csv.

    Returns:
        The same dict with converted values.
    """
    # TODO: convert quantity to int, unit_price to float, order_date to datetime.date
    pass


def clean_data(rows: list[dict]) -> list[dict]:
    """Apply clean_row to every row and drop any rows where cleaning fails.

    Args:
        rows: Raw rows from load_csv.

    Returns:
        A list of cleaned rows.
    """
    # TODO: apply clean_row to each row; skip rows that raise a ValueError or KeyError
    pass


# ---------------------------------------------------------------------------
# Calculations
# ---------------------------------------------------------------------------

def calculate_revenue(row: dict) -> float:
    """Return the total revenue for a single order row.

    Revenue = quantity * unit_price

    Args:
        row: A cleaned row dict.

    Returns:
        Revenue as a float.
    """
    # TODO: implement this function
    pass


# ---------------------------------------------------------------------------
# Filtering
# ---------------------------------------------------------------------------

def filter_by_region(rows: list[dict], region: str) -> list[dict]:
    """Return only the rows that match the given region (case-insensitive).

    Args:
        rows: Cleaned rows.
        region: The region name to filter by.

    Returns:
        Filtered list of rows.
    """
    # return only rows where the region matches the given region string (case-insensitive)
    pass


# ---------------------------------------------------------------------------
# Summarisation
# ---------------------------------------------------------------------------

def summarise_by_category(rows: list[dict]) -> dict[str, float]:
    """Return a dictionary mapping each category to its total revenue.

    Args:
        rows: Cleaned rows (already processed by calculate_revenue is not required;
              this function should compute revenue internally).

    Returns:
        Dict of {category: total_revenue}.
    """
    pass
