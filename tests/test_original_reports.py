"""Regressionstest: rapporterna ska matcha originalprogrammets CSV-utdata."""
from pathlib import Path

import pandas as pd
import pytest

from order_report.config import (
    CATEGORY_REPORT_PATH, INPUT_CSV, REGION_REPORT_PATH,
    RETURNS_REPORT_PATH, SUMMARY_REPORT_PATH,
)
from order_report.loading import ladda_orderdata
from order_report.validation import rensa_och_validera_data
from order_report.processing import generera_fyra_rapporter
from order_report.reporting import spara_rapport_till_csv

EXPECTED_DIR = Path(__file__).parent / "expected"


@pytest.mark.parametrize("key,filename,configured_path", [
    ("summary", "overview.csv", SUMMARY_REPORT_PATH),
    ("category", "sales_by_category.csv", CATEGORY_REPORT_PATH),
    ("region", "sales_by_region.csv", REGION_REPORT_PATH),
    ("returns", "returns_by_category.csv", RETURNS_REPORT_PATH),
])
def test_report_matches_original(key, filename, configured_path, tmp_path):
    assert configured_path.name == filename
    cleaned = rensa_och_validera_data(ladda_orderdata(INPUT_CSV))
    reports = generera_fyra_rapporter(cleaned)
    actual_path = tmp_path / filename
    spara_rapport_till_csv(reports[key], actual_path)
    actual = pd.read_csv(actual_path)
    expected = pd.read_csv(EXPECTED_DIR / filename)
    pd.testing.assert_frame_equal(actual, expected, check_dtype=False)
