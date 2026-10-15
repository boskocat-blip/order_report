
import pandas as pd
from typing import List, Dict

from order_report.config import logger
from order_report.models import Order


def konvertera_till_order_objekt(
    df: pd.DataFrame
) -> List[Order]:
    """
    Konverterar rensad data till Order-objekt.
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
            returned=bool(row["returned"]),
        )
        order_lista.append(order)

    return order_lista


def generera_fyra_rapporter(
    df: pd.DataFrame
) -> Dict[str, pd.DataFrame]:
    """
    Skapar fyra rapporter med samma beräkningar
    och kolumner som originalprogrammet.
    """
    data = df.copy()

    # Beräkna ordervärde och rabatterat värde
    data["order_value"] = (
        data["quantity"] * data["unit_price"]
    )

    data["discounted_value"] = (
        data["order_value"] * (1 - data["discount"])
    )

    # 1. Overview
    total_sales = round(
        data["discounted_value"].sum(), 2
    )

    number_of_orders = data["order_id"].nunique()
    number_of_returns = int(data["returned"].sum())

    overview = pd.DataFrame({
        "metric": [
            "total_sales",
            "order_count",
            "return_count",
        ],
        "value": [
            total_sales,
            number_of_orders,
            number_of_returns,
        ],
    })

    # 2. Sales by category
    category_df = (
        data.groupby(
            "product_category", as_index=False
        )
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("discounted_value", "sum"),
            returns=("returned", "sum"),
        )
    )

    category_df["total_sales"] = (
        category_df["total_sales"].round(2)
    )

    category_df["return_rate"] = (
        category_df["returns"]
        / category_df["order_count"]
    ).round(3)

    category_df = (
        category_df
        .sort_values("total_sales", ascending=False)
        .reset_index(drop=True)
    )

    # 3. Sales by region
    region_df = (
        data.groupby(
            "region", as_index=False
        )
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("discounted_value", "sum"),
            returns=("returned", "sum"),
        )
    )

    region_df["total_sales"] = (
        region_df["total_sales"].round(2)
    )

    region_df["return_rate"] = (
        region_df["returns"]
        / region_df["order_count"]
    ).round(3)

    region_df = (
        region_df
        .sort_values("total_sales", ascending=False)
        .reset_index(drop=True)
    )

    # 4. Returns by category
    returns_df = (
        data.groupby(
            "product_category", as_index=False
        )
        .agg(
            order_count=("order_id", "nunique"),
            returns=("returned", "sum"),
        )
    )

    returns_df["return_rate"] = (
        returns_df["returns"]
        / returns_df["order_count"]
    ).round(3)

    returns_df = (
        returns_df
        .sort_values("return_rate", ascending=False)
        .reset_index(drop=True)
    )

    logger.info(
        "Alla fyra rapporter har beräknats."
    )

    return {
        "summary": overview,
        "category": category_df,
        "region": region_df,
        "returns": returns_df,
    }
