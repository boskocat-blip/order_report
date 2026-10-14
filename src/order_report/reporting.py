import pandas as pd
from pathlib import Path
from order_report.config import logger

def spara_rapport_till_csv(df: pd.DataFrame, output_path: Path) -> None:
    """
    Sparar en DataFrame till en CSV-fil.
    """
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
        logger.info(f"Rapport sparad till CSV: {output_path}")
    except Exception as e:
        logger.error(f"Misslyckades att spara rapporten till {output_path}: {e}")
        raise