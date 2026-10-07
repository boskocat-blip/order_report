import pytest
import pandas as pd
from order_report.validation import validera_kolumner, rensa_och_validera_data

def test_validera_kolumner_saknas_kastar_fel():
    df_incomplete = pd.DataFrame({"order_id": [1], "region": ["Nord"]})
    with pytest.raises(ValueError):
        validera_kolumner(df_incomplete)

def test_rensa_och_validera_data_framgangsrik():
    data = {
        "order_id": [1],
        "order_date": ["2026-01-01"],
        "customer_id": [101],
        "region": ["Nord"],
        "product_category": ["Elektronik"],
        "quantity": ["2"],
        "unit_price": ["500.0"],
        "discount": ["0.1"],
        "returned": ["False"]
    }
    df = pd.DataFrame(data)
    df_rensad = rensa_och_validera_data(df)
    assert df_rensad["quantity"].iloc[0] == 2
    assert df_rensad["unit_price"].iloc[0] == 500.0
    assert not df_rensad["returned"].iloc[0]