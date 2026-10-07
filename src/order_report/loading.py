import pandas as pd
from pathlib import Path
from order_report.config import logger

def ladda_orderdata(filsokvag: Path) -> pd.DataFrame:
    """
    Läser in orderdata från en CSV-fil till en Pandas DataFrame.
    """
    if not filsokvag.exists():
        logger.error(f"Filen kunde inte hittas: {filsokvag}")
        raise FileNotFoundError(f"Filen finns inte: {filsokvag}")
    
    try:
        df = pd.read_csv(filsokvag)
        logger.info(f"Data har lästs in framgångsrikt från {filsokvag}")
        return df
    except Exception as e:
        logger.error(f"Ett fel uppstod vid inläsning av CSV-filen: {e}")
        raise