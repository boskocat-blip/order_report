# Orderrapportering - Refaktorerat Pythonprogram

Detta projekt är en refaktorerat och modulär Python-applikation för att bearbeta orderdata från en CSV-fil och generera fyra ursprungliga CSV-rapporter.

## Projektstruktur
```text
order_report_project/
├── README.md
├── code_review.md
├── reflection.md
├── requirements.txt
├── data/
│   └── orders.csv
├── output/
│   ├── summary_report.csv
│   ├── category_report.csv
│   ├── region_report.csv
│   └── returns_report.csv
├── src/
│   └── order_report/
│       ├── __init__.py
│       ├── config.py
│       ├── models.py
│       ├── loading.py
│       ├── validation.py
│       ├── processing.py
│       └── reporting.py
├── main.py
└── tests/
    ├── test_processing.py
    └── test_validation.py