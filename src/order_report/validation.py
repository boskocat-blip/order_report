
import pandas as pd
from order_report.config import logger


NODVANDIGA_KOLUMNER = [
    "order_id",
    "order_date",
    "customer_id",
    "region",
    "product_category",
    "quantity",
    "unit_price",
    "discount",
    "returned",
]


def validera_kolumner(df: pd.DataFrame) -> bool:
    """
    Kontrollerar att alla nödvändiga kolumner finns.
    """
    saknade = [
        kol for kol in NODVANDIGA_KOLUMNER
        if kol not in df.columns
    ]

    if saknade:
        logger.error(f"Saknade kolumner: {saknade}")
        raise ValueError(
            f"Datan saknar följande nödvändiga kolumner: {saknade}"
        )

    return True


def rensa_och_validera_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rensar data enligt originalprogrammets regler.
    """
    validera_kolumner(df)

    df_rensad = df.copy()

    # Normalisera regioner
    df_rensad["region"] = (
        df_rensad["region"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    # Normalisera produktkategorier
    df_rensad["product_category"] = (
        df_rensad["product_category"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    # Saknad kvantitet ersätts med 1
    df_rensad["quantity"] = pd.to_numeric(
        df_rensad["quantity"], errors="coerce"
    ).fillna(1)

    # Saknat pris ersätts med medianen
    df_rensad["unit_price"] = pd.to_numeric(
        df_rensad["unit_price"], errors="coerce"
    )

    df_rensad["unit_price"] = (
        df_rensad["unit_price"]
        .fillna(df_rensad["unit_price"].median())
    )

    # Saknad rabatt ersätts med 0
    df_rensad["discount"] = pd.to_numeric(
        df_rensad["discount"], errors="coerce"
    ).fillna(0)

    # Omvandla returvärden till True eller False
    df_rensad["returned"] = (
        df_rensad["returned"]
        .fillna("false")
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(["true", "yes", "1", "ja"])
    )

    logger.info(
        "Datavalidering och datarensning genomförd."
    )

    return df_rensad
