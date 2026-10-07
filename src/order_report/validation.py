import pandas as pd
from order_report.config import logger

NÖDVÄNDIGA_KOLUMNER = [
    "order_id", "order_date", "customer_id", "region",
    "product_category", "quantity", "unit_price", "discount", "returned"
]

def validera_kolumner(df: pd.DataFrame) -> bool:
    """
    Kontrollerar att alla nödvändiga kolumner finns i DataFrame.
    """
    saknade = [kol for kol in NÖDVÄNDIGA_KOLUMNER if kol not in df.columns]
    if saknade:
        logger.error(f"Saknade kolumner i datan: {saknade}")
        raise ValueError(f"Datan saknar följande nödvändiga kolumner: {saknade}")
    return True

def rensa_och_validera_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Hanterar saknade värden och validerar datatyper.
    """
    validera_kolumner(df)
    
    df_rensad = df.copy()
    
    # Omvandla numeriska kolumner och fyll i saknade värden vid behov
    df_rensad["quantity"] = pd.to_numeric(df_rensad["quantity"], errors="coerce").fillna(0)
    df_rensad["unit_price"] = pd.to_numeric(df_rensad["unit_price"], errors="coerce").fillna(0.0)
    df_rensad["discount"] = pd.to_numeric(df_rensad["discount"], errors="coerce").fillna(0.0)
    df_rensad["returned"] = df_rensad["returned"].astype(str).str.lower().isin(["true", "1", "yes"])
    
    logger.info("Datavalidering och datarensning genomförd.")
    return df_rensad