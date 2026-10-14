import pytest
import pandas as pd
from order_report.models import Order
from order_report.processing import generera_fyra_rapporter, konvertera_till_order_objekt

def test_order_dataclass_properties():
    order = Order(
        order_id="101",
        order_date="2026-01-01",
        customer_id="C1",
        region="Nord",
        product_category="Elektronik",
        quantity=2,
        unit_price=100.0,
        discount=0.1,
        returned=False
    )
    assert order.brutto_total == 200.0
    assert order.net_total == 180.0

def test_generera_fyra_rapporter():
    df = pd.DataFrame({
        "order_id": [1, 2],
        "order_date": ["2026-01-01", "2026-01-02"],
        "customer_id": [101, 102],
        "region": ["Nord", "Syd"],
        "product_category": ["Elektronik", "Klader"],
        "quantity": [2, 1],
        "unit_price": [100.0, 200.0],
        "discount": [0.1, 0.0],
        "returned": [False, True]
    })
    
    rapporter = generera_fyra_rapporter(df)
    
    assert "summary" in rapporter
    assert "category" in rapporter
    assert "region" in rapporter
    assert "returns" in rapporter
    
    summary_df = rapporter["summary"]
    sales_row = summary_df[summary_df["metric"] == "Total Sales (Net)"]
    assert sales_row["value"].values[0] == 180.0