import pytest
import pandas as pd
from order_report.processing import berakna_ordervarden, sammanstall_forsaljning

def test_berakna_ordervarden():
    df = pd.DataFrame({
        "quantity": [2, 1],
        "unit_price": [100.0, 200.0],
        "discount": [0.1, 0.0]
    })
    df_res = berakna_ordervarden(df)
    assert df_res["brutto_total"].tolist() == [200.0, 200.0]
    assert df_res["rabatterat_varde"].tolist() == [180.0, 200.0]

def test_sammanstall_forsaljning_exkluderar_returer():
    df = pd.DataFrame({
        "order_id": [1, 2],
        "order_date": ["2026-01-01", "2026-01-02"],
        "customer_id": [101, 102],
        "region": ["Nord", "Syd"],
        "product_category": ["Elektronik", "Klader"],
        "quantity": [1, 1],
        "unit_price": [100.0, 100.0],
        "discount": [0.0, 0.0],
        "returned": [False, True]  # En retur
    })
    rapport = sammanstall_forsaljning(df)
    assert rapport["total_forsaljning"] == 100.0