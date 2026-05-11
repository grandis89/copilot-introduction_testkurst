"""
ETL Pipeline Stub — Bonus Exercise

This is a minimal skeleton. Use Copilot Agent Mode to build it out.
See exercises/bonus/README.md for the full instructions and prompt.
"""

import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent.parent / "data"
REPORTS_DIR = Path(__file__).parent.parent.parent / "reports"
SOURCE_FILE = DATA_DIR / "sales_sample.csv"


def extract(file_path: Path):
    """Load raw data from a CSV file."""
    # TODO: implement
    pass


def transform(raw_rows):
    """Clean, validate, and enrich the raw rows."""
    # TODO: implement
    pass


def summarise(clean_rows):
    """Produce the three summary datasets."""
    # TODO: return revenue_by_region, top_products, monthly_trend
    pass


def load(revenue_by_region, top_products, monthly_trend, output_dir: Path) -> None:
    """Write summary CSVs to the output directory."""
    # TODO: implement
    pass


def main() -> None:
    logger.info("Starting ETL pipeline")
    raw = extract(SOURCE_FILE)
    clean = transform(raw)
    region_summary, top_prods, monthly = summarise(clean)
    REPORTS_DIR.mkdir(exist_ok=True)
    load(region_summary, top_prods, monthly, REPORTS_DIR)
    logger.info("Pipeline complete")


if __name__ == "__main__":
    main()
