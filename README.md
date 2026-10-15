# Orderrapportering – Refaktorerat Pythonprogram

Detta projekt är en refaktorerad och modulär Python-applikation som läser orderdata från en CSV-fil, validerar och bearbetar informationen samt genererar fyra CSV-rapporter.

## Projektstruktur

```text
order_report_project/
├── main.py
├── pyproject.toml
├── README.md
├── data/
│   └── orders.csv
├── output/
│   ├── overview.csv
│   ├── sales_by_category.csv
│   ├── sales_by_region.csv
│   └── returns_by_category.csv
├── src/
│   └── order_report/
│       ├── __init__.py
│       ├── config.py
│       ├── models.py
│       ├── loading.py
│       ├── validation.py
│       ├── processing.py
│       └── reporting.py
└── tests/
    ├── test_processing.py
    └── test_validation.py
```

## Installation

Python 3.10 eller senare krävs.

Öppna terminalen i projektets huvudmapp och installera projektet med:

```bash
python -m pip install -e .
```

## Kör programmet

Kör följande kommando:

```bash
python main.py
```

Programmet läser `data/orders.csv` och sparar fyra rapporter i mappen `output`.

## Rapporter

- `overview.csv` – sammanfattning av försäljning, antal order och returer.
- `sales_by_category.csv` – försäljning per produktkategori.
- `sales_by_region.csv` – försäljning per region.
- `returns_by_category.csv` – returer per produktkategori.

## Datavalidering

Programmet kontrollerar att nödvändiga kolumner finns, hanterar saknade numeriska värden och normaliserar regioner och produktkategorier. Returvärden omvandlas till booleska värden.

## Testning

Installera pytest vid behov:

```bash
python -m pip install pytest
```

Kör testerna med:

```bash
python -m pytest -v
```

## Kodstruktur

Koden är uppdelad i moduler för konfiguration, datainläsning, validering, bearbetning och rapportgenerering. En dataclass används för att representera en order. Logging används för att dokumentera programmets körning och fel.
