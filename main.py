import sys
from pathlib import Path

# Lägg till 'src' i sys.path för korrekt modulimport
sys.path.append(str(Path(__file__).resolve().parent / "src"))

from order_report.config import (
    INPUT_CSV,
    SUMMARY_REPORT_PATH,
    CATEGORY_REPORT_PATH,
    REGION_REPORT_PATH,
    RETURNS_REPORT_PATH,
    logger
)
from order_report.loading import ladda_orderdata
from order_report.validation import rensa_och_validera_data
from order_report.processing import konvertera_till_order_objekt, generera_fyra_rapporter
from order_report.reporting import spara_rapport_till_csv

def main():
    logger.info("Startar orderrapporteringsprogrammet...")

    try:
        # 1. Ladda data
        raw_df = ladda_orderdata(INPUT_CSV)

        # 2. Validera och rensa data
        clean_df = rensa_och_validera_data(raw_df)

        # 3. Använd dataclass för objektorienterad struktur
        orders = konvertera_till_order_objekt(clean_df)
        logger.info(f"Totalt {len(orders)} orderobjekt skapades.")

        # 4. Bearbeta data och skapa 4 CSV-rapporter
        rapporter = generera_fyra_rapporter(clean_df)

        # 5. Spara de fyra CSV-rapporterna
        spara_rapport_till_csv(rapporter["summary"], SUMMARY_REPORT_PATH)
        spara_rapport_till_csv(rapporter["category"], CATEGORY_REPORT_PATH)
        spara_rapport_till_csv(rapporter["region"], REGION_REPORT_PATH)
        spara_rapport_till_csv(rapporter["returns"], RETURNS_REPORT_PATH)

        logger.info("Programmet har slutförts framgångsrikt och alla 4 CSV-rapporter har skapats.")

    except Exception as e:
        logger.critical(f"Programmet avbröts på grund av ett fel: {e}")

if __name__ == "__main__":
    main()