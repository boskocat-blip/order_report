import pandas as pd
from order_report.config import logger

def berakna_ordervarden(df: pd.DataFrame) -> pd.DataFrame:
    """
    Beräknar brutto- och nettototalsumma (rabatterat värde) för varje order.
    """
    df_resultat = df.copy()
    df_resultat["brutto_total"] = df_resultat["quantity"] * df_resultat["unit_price"]
    df_resultat["rabatterat_varde"] = df_resultat["brutto_total"] * (1 - df_resultat["discount"])
    return df_resultat

def sammanstall_forsaljning(df: pd.DataFrame) -> dict:
    """
    Sammanställer försäljningsstatistik per produktkategori och region.
    Exkluderar returnerade ordrar från total försäljning.
    """
    df_bereknad = berakna_ordervarden(df)
    godkanda_ordrar = df_bereknad[~df_bereknad["returned"]]
    
    total_forsaljning = float(godkanda_ordrar["rabatterat_varde"].sum())
    per_kategori = godkanda_ordrar.groupby("product_category")["rabatterat_varde"].sum().to_dict()
    per_region = godkanda_ordrar.groupby("region")["rabatterat_varde"].sum().to_dict()
    
    logger.info("Försäljningsdata sammanställd.")
    return {
        "total_forsaljning": round(total_forsaljning, 2),
        "forsaljning_per_kategori": {k: round(v, 2) for k, v in per_kategori.items()},
        "forsaljning_per_region": {k: round(v, 2) for k, v in per_region.items()}
    }

def sammanstall_returer(df: pd.DataFrame) -> dict:
    """
    Sammanställer returstatistik och returgrad.
    """
    total_ordrar = len(df)
    returer = df[df["returned"]]
    antal_returer = len(returer)
    returgrad = (antal_returer / total_ordrar) * 100 if total_ordrar > 0 else 0.0
    
    returer_per_kategori = returer.groupby("product_category")["order_id"].count().to_dict()
    
    logger.info("Returdata sammanställd.")
    return {
        "totalt_antal_ordrar": total_ordrar,
        "antal_returer": antal_returer,
        "returgrad_procent": round(returgrad, 2),
        "returer_per_kategori": returer_per_kategori
    }