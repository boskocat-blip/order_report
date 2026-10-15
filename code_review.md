# Kodgranskning (Code Review)

Detta dokument innehåller en granskning av den ursprungliga koden för orderrapportering.

## 1. Monolitisk struktur och bristande ansvarsfördelning

- **Observation:** All kod (CSV-inläsning, datarensning, beräkningar och filskrivning) låg samlad i en monolitisk skriptfil.
- **Konsekvens:** Koden var svår att läsa, underhålla och testa isolerat.
- **Förslag:** Dela upp programmet i modulära komponenter (`loading.py`, `validation.py`, `processing.py`, `reporting.py`, `models.py`).

## 2. Användning av `print()` istället för strukturerad loggning

- **Observation:** Utskrifter gjordes direkt med `print()`.
- **Konsekvens:** Utskrifterna saknade tidsstämplar, loggnivåer (INFO, ERROR) och möjlighet att omdirigera loggar vid produktionsdrift.
- **Förslag:** Implementera Pythons inbyggda `logging`-modul.

## 3. Saknad av felhantering och datavalidering

- **Observation:** Programmet förutsatte att CSV-filen och dess kolumner alltid var korrekta.
- **Konsekvens:** Koden kunde krascha oväntat vid saknade filer, felaktiga datatyper eller tomma värden.
- **Förslag:** Inför explicita valideringsfunktioner och `try-except`-block vid filhantering.

## 4. Saknad av objektorienterad struktur (`dataclass`)

- **Observation:** Datan hanterades enbart som råa rader utan strukturell modellering.
- **Konsekvens:** Det fanns ingen tydlig domänmodell för vad en Order representerar i koden.
- **Förslag:** Skapa en `@dataclass Order` i `models.py` för att kapsla in orderegenskaper och beräkningar som `brutto_total` och `net_total`.

## 5. Saknad av automatiska tester

- **Observation:** Det fanns inga enhetstester för att verifiera beräkningar eller validering.
- **Konsekvens:** Det fanns en hög risk för regressionsfel vid vidareutveckling.
- **Förslag:** Skriv enhetstester med `pytest` i mappen `tests/`.