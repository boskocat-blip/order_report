# Orderrapportering - refaktorerat Pythonprogram

Det här är min lösning på den individuella uppgiften i Python-fördjupningen. Jag har tagit över ett litet skript som läser orderdata från en CSV-fil och skapar rapporter, och byggt om det så att det är lättare att läsa, testa och bygga vidare på. Rapporternas siffror ska vara exakt desamma som i originalet. Det är bara själva uppbyggnaden som har ändrats.

## Vad programmet gör

1. Läser `data/orders.csv` (80 rader, 9 kolumner).
2. Kontrollerar att alla nödvändiga kolumner finns.
3. Rensar datan: trimmar och normaliserar `region` och `product_category`, fyller i saknade värden och gör om `returned` till True/False.
4. Räknar ut ordervärde (`quantity * unit_price`) och rabatterat värde (`order_value * (1 - discount)`).
5. Skapar fyra rapporter och sparar dem som CSV i `output/`.

### Hur saknade värden hanteras

Det här är samma regler som originalskriptet använde, och jag har medvetet inte ändrat dem:

| Kolumn | Om värdet saknas eller är fel |
|---|---|
| `region`, `product_category` | blir `Unknown` |
| `quantity` | blir `1` |
| `unit_price` | blir medianen av alla priser |
| `discount` | blir `0` |
| `returned` | `true`, `yes`, `1`, `ja` räknas som retur, allt annat som ingen retur |

### Rapporterna

| Fil | Innehåll |
|---|---|
| `overview.csv` | total försäljning, antal order och antal returer |
| `sales_by_category.csv` | order, försäljning, returer och returandel per produktkategori |
| `sales_by_region.csv` | samma sak per region |
| `returns_by_category.csv` | returer och returandel per kategori, sorterat på returandel |

## Kom igång

Projektet är gjort för Python 3.13. Beroenden är `pandas` (för programmet) och `pytest` (för testerna).

```bash
# 1. (valfritt men rekommenderat) skapa en virtuell miljö
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. installera projektet och beroenden
python -m pip install -e .
python -m pip install -r requirements.txt
```

Steg 2 är viktigt. `pip install -e .` gör att `order_report` går att importera överallt, både från `main.py` och från testerna, utan att jag behöver pilla med `sys.path`.

## Köra programmet

```bash
python main.py
```

Programmet loggar vad som händer i terminalen (inläsning, validering, antal order, var rapporterna sparas) och skriver de fyra CSV-filerna till `output/`.

## Köra testerna

```bash
python -m pytest -v
```

Det finns åtta tester:

- **`test_processing.py`** (2 st): kollar att `Order`-dataklassens `brutto_total` och `net_total` räknar rätt (2 × 100 med 10 % rabatt blir 180), och att rapporterna får rätt struktur och rätt `total_sales` på en liten testdata.
- **`test_validation.py`** (2 st): kollar att en saknad kolumn ger `ValueError` (felscenariot), och att rensningen gör om textvärden till rätt typer.
- **`test_original_reports.py`** (4 st): regressionstester. De kör hela flödet på `orders.csv` och jämför varje rapport med originalprogrammets utdata i `tests/expected/`. Det är de här som visar att refaktoreringen inte har ändrat några resultat.

## Projektstruktur

```text
order_report/
├── main.py                  # startpunkten, kör hela flödet
├── pyproject.toml           # paketinställningar och beroenden
├── requirements.txt         # pandas + pytest
├── README.md
├── code_review.md           # granskning av originalkoden
├── reflection.md            # min reflektion
├── data/
│   └── orders.csv           # indata
├── original/
│   └── order_report.py      # det ursprungliga skriptet, sparat som referens
├── output/                  # här hamnar rapporterna när programmet körs
├── src/order_report/
│   ├── config.py            # sökvägar och logging-inställningar
│   ├── models.py            # Order-dataklassen
│   ├── loading.py           # läser CSV-filen
│   ├── validation.py        # kolumnkontroll och datarensning
│   ├── processing.py        # beräkningar och de fyra rapporterna
│   └── reporting.py         # sparar rapporterna till CSV
└── tests/
    ├── test_processing.py
    ├── test_validation.py
    ├── test_original_reports.py
    └── expected/            # referensrapporter från originalprogrammet
```

Flödet i `main.py` följer samma ordning som mapparna: **läsa in → validera och rensa → bearbeta → spara**. Den som vill hitta var något händer kan alltså gå direkt till rätt modul.

## Några tekniska val

- **Modulstruktur med `src/`-layout.** Varje modul har ett tydligt ansvar, och jag har inte delat upp mer än nödvändigt.
- **Dataclass för `Order`.** Den samlar orderns fält och beräkningarna `brutto_total` och `net_total` på ett ställe.
- **Logging i stället för `print()`.** Meddelandena har nivåer (INFO, ERROR, CRITICAL) och tidsstämplar.
- **Fel som syns.** Saknad fil och saknade kolumner ger tydliga felmeddelanden (`FileNotFoundError` respektive `ValueError` som listar vilka kolumner som saknas).

## Mer att läsa

- [`code_review.md`](code_review.md) - vad som var problematiskt i originalkoden och hur jag löste det
- [`reflection.md`](reflection.md) - min reflektion över arbetet
