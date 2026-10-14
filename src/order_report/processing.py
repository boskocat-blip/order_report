import pandas as pd
from typing import List, Dict
from order_report.config import logger
from order_report.models import Order

def konvertera_till_order_objekt(df: pd.DataFrame) -> List[Order]:
    """
    Konverterar en rensad DataFrame till en lista av Order-objekt (Dataclass).
    """
    order_lista = []
    for _, row in df.iterrows():
        order = Order(
            order_id=str(row["order_id"]),
            order_date=str(row["order_date"]),
            customer_id=str(row["customer_id"]),
            region=str(row["region"]),
            product_category=str(row["product_category"]),
            quantity=int(row["quantity"]),
            unit_price=float(row["unit_price"]),
            discount=float(row["discount"]),
            returned=bool(row["returned"])
        )
        order_lista.append(order)
    return order_lista

def generera_fyra_rapporter(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """
    Genererar de fyra ursprungliga rapport-DataFrames med exakt samma beräkningar.
    """
    df_calc = df.copy()
    df_calc["brutto_total"] = df_calc["quantity"] * df_calc["unit_price"]
    df_calc["net_total"] = df_calc["brutto_total"] * (1.0 - df_calc["discount"])

    # 1. Summary report
    godkanda = df_calc[~df_calc["returned"]]
    totalt_forsaljning = godkanda["net_total"].sum()
    totalt_antal_ordrar = len(df_calc)
    antal_returer = df_calc["returned"].sum()
    returgrad = (antal_returer / totalt_antal_ordrar * 100) if totalt_antal_ordrar > 0 else 0.0

    summary_df = pd.DataFrame({
        "metric": ["Total Sales (Net)", "Total Orders", "Total Returns", "Return Rate (%)"],
        "value": [round(totalt_forsaljning, 2), totalt_antal_ordrar, antal_returer, round(returgrad, 2)]
    })

    # 2. Category report
    category_df = godkanda.groupby("product_category")["net_total"].sum().reset_index()
    category_df.columns = ["product_category", "total_sales"]
    category_df["total_sales"] = category_df["total_sales"].round(2)

    # 3. Region report
    region_df = godkanda.groupby("region")["net_total"].sum().reset_index()
    region_df.columns = ["region", "total_sales"]
    region_df["total_sales"] = region_df["total_sales"].round(2)

    # 4. Returns report
    returns_df = df_calc.groupby("product_category")["returned"].agg(
        total_orders="count",
        returned_orders="sum"
    ).reset_index()
    returns_df["return_rate_percent"] = (returns_df["returned_orders"] / returns_df["total_orders"] * 100).round(2)

    logger.info("Alla 4 rapporter har beräknats framgångsrikt.")
    return {
        "summary": summary_df,
        "category": category_df,
        "region": region_df,
        "returns": returns_df
    }