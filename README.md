# Orderrapporteringssystem

Detta projekt är en refaktorerad och modulariserad Python-applikation för att bearbeta orderdata, hantera fel/validering samt generera försäljnings- och returrapporter.

## Projektstruktur
- `src/order_report/`: Innehåller programmets källkod uppdelad i moduler.
- `data/`: Innehåller indatafilen `orders.csv`.
- `output/`: Mapp där genererade rapporter sparas.
- `tests/`: Innehåller automatiska enhetstester skrivna i `pytest`.

## Installation och Körning

1. Skapa och aktivera en virtuell miljö (valfritt men rekommenderas):
   ```bash
   python -m venv venv
   source venv/bin/activate  # På Windows: venv\Scripts\activate