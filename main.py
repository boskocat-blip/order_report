import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent / "src"))

from order_report.config import (
    INPUT_CSV,
    SALES_REPORT_PATH,
    RETURNS_REPORT_PATH,
    logger,
)
from order_report.loading import ladda_orderdata
from order_report.validation import rensa_och_validera_data
from order_report.processing import sammanstall_forsaljning, sammanstall_returer
from order_report.reporting import spara_rapport_till_json


def main():
    logger.info("Startar orderrapporteringsprogrammet...")

    try:
        # 1. Ladda data
        raw_df = ladda_orderdata(INPUT_CSV)

        # 2. Validera och rensa data
        clean_df = rensa_och_validera_data(raw_df)

        # 3. Bearbeta data
        forsaljnings_rapport = sammanstall_forsaljning(clean_df)
        retur_rapport = sammanstall_returer(clean_df)

        # 4. Spara rapporter
        spara_rapport_till_json(forsaljnings_rapport, SALES_REPORT_PATH)
        spara_rapport_till_json(retur_rapport, RETURNS_REPORT_PATH)

        logger.info("Programmet har slutförts framgångsrikt.")

    except Exception as e:
        logger.critical(f"Programmet avbröts på grund av ett fel: {e}")


if __name__ == "__main__":
    main()