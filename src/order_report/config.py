import logging
from pathlib import Path

# Sökvägar för projektet
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

INPUT_CSV = DATA_DIR / "orders.csv"
SALES_REPORT_PATH = OUTPUT_DIR / "forsaljningsrapport.json"
RETURNS_REPORT_PATH = OUTPUT_DIR / "returrapport.json"

# Konfiguration för loggning
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s"
)
logger = logging.getLogger("order_report")