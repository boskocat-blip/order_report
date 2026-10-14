import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

INPUT_CSV = DATA_DIR / "orders.csv"

# Fyra ursprungliga CSV-rapporter
SUMMARY_REPORT_PATH = OUTPUT_DIR / "summary_report.csv"
CATEGORY_REPORT_PATH = OUTPUT_DIR / "category_report.csv"
REGION_REPORT_PATH = OUTPUT_DIR / "region_report.csv"
RETURNS_REPORT_PATH = OUTPUT_DIR / "returns_report.csv"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s"
)
logger = logging.getLogger("order_report")