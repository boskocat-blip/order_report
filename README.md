# Orderrapportering – Refaktorerat Pythonprogram

Detta projekt är en refaktorerad och modulär Python-applikation som läser orderdata från en CSV-fil, validerar och bearbetar informationen samt genererar fyra CSV-rapporter.

Syftet med refaktoreringen är att förbättra kodens struktur, läsbarhet, underhållbarhet och testbarhet, samtidigt som originalprogrammets rapporter och beräkningar bevaras.

## Projektstruktur

```text
order_report_project/
├── main.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── code_review.md
├── reflection.md
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
    ├── test_validation.py
    ├── test_original_reports.py
    └── expected/
        ├── overview.csv
        ├── sales_by_category.csv
        ├── sales_by_region.csv
        └── returns_by_category.csv
```

## Installation

Python 3.10 eller senare krävs.

Öppna terminalen i projektets huvudmapp och installera projektet med:

```bash
python -m pip install -e .
```

Installera även testberoenden vid behov:

```bash
python -m pip install -r requirements.txt
```

## Kör programmet

Kör följande kommando:

```bash
python main.py
```

Programmet läser `data/orders.csv` och sparar fyra rapporter i mappen `output/`.

## Rapporter

- `overview.csv` – sammanfattning av försäljning, antal order och returer.
- `sales_by_category.csv` – försäljning per produktkategori.
- `sales_by_region.csv` – försäljning per region.
- `returns_by_category.csv` – returer per produktkategori.

Rapporterna ska behålla originalprogrammets filnamn, kolumner, beräkningar och resultat.

## Datavalidering och bearbetning

Programmet kontrollerar att nödvändiga kolumner finns, hanterar saknade numeriska värden och normaliserar regioner och produktkategorier. Returvärden omvandlas till booleska värden.

Försäljningen beräknas med hänsyn till rabatter, och returer hanteras i rapporternas sammanställningar enligt originalprogrammets logik.

## Testning

Projektet innehåller åtta automatiserade tester som körs med pytest.

Kör testerna med:

```bash
python -m pytest -v
```

Fyra tester kontrollerar programmets bearbetning och validering. Ytterligare fyra tester i `test_original_reports.py` kontrollerar att de genererade CSV-rapporterna överensstämmer med referensfilerna från originalprogrammet.

Referensfilerna finns i `tests/expected/` och används för att verifiera att rapporternas innehåll, kolumner och resultat bevaras efter refaktoreringen.

Samtliga åtta tester har körts lokalt med godkänt resultat.

## Kodstruktur

Koden är uppdelad i moduler för konfiguration, datainläsning, validering, bearbetning och rapportgenerering.

En dataclass används för att representera en order. Logging används för att dokumentera programmets körning och fel.

## Dokumentation

- code_review.md – kodgranskning med identifierade förbättringsområden, konsekvenser och förslag.
- reflection.md – reflektion kring refaktoreringen, genomförandet och lärdomarna.
- requirements.txt och pyproject.toml – beroenden och projektkonfiguration.

