"""
Sales data transformation utilities — reference solution.

Do not open this file until you have tried the exercise yourself!
"""

import csv
import datetime
from pathlib import Path


def load_csv(file_path: Path) -> list[dict]:
    """Load a CSV file and return a list of row dictionaries."""
    rows = []
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(dict(row))
    return rows


def clean_row(row: dict) -> dict:
    """Convert raw string values in a row to the correct Python types."""
    row["quantity"] = int(row["quantity"])
    row["unit_price"] = float(row["unit_price"])
    row["order_date"] = datetime.date.fromisoformat(row["order_date"])
    return row


def clean_data(rows: list[dict]) -> list[dict]:
    """Apply clean_row to every row and drop any rows where cleaning fails."""
    cleaned = []
    for row in rows:
        try:
            cleaned.append(clean_row(row))
        except (ValueError, KeyError):
            pass
    return cleaned


def calculate_revenue(row: dict) -> float:
    """Return the total revenue for a single order row."""
    return row["quantity"] * row["unit_price"]


def filter_by_region(rows: list[dict], region: str) -> list[dict]:
    """Return only the rows that match the given region (case-insensitive)."""
    return [row for row in rows if row["region"].lower() == region.lower()]


def summarise_by_category(rows: list[dict]) -> dict[str, float]:
    """Return a dictionary mapping each category to its total revenue."""
    summary: dict[str, float] = {}
    for row in rows:
        category = row["category"]
        revenue = calculate_revenue(row)
        summary[category] = summary.get(category, 0.0) + revenue
    return summary


def main() -> None:
    data_path = Path(__file__).parent.parent.parent / "data" / "sales_sample.csv"
    raw = load_csv(data_path)
    clean = clean_data(raw)
    summary = summarise_by_category(clean)
    for category, total in sorted(summary.items(), key=lambda x: -x[1]):
        print(f"{category:<20} NOK {total:>10,.2f}")


if __name__ == "__main__":
    main()
