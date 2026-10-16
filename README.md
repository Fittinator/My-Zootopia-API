# My-Zootopia-API

Ein Python-Lernprojekt, das Tierinformationen von der [Animals API von API Ninjas](https://api-ninjas.com/api/animals) abruft und daraus eine HTML-Webseite erstellt. Du gibst einen Tiernamen ein und erhältst Karten mit den gefundenen Tieren, ihrer Ernährung, ihrem ersten Standort und ihrem Typ, soweit diese Angaben verfügbar sind.

Das Projekt richtet sich an Python-Einsteiger, die API-Abfragen, Umgebungsvariablen und die Aufteilung eines Programms in mehrere Dateien kennenlernen möchten.

## Voraussetzungen

- Python 3 und Git
- Internetverbindung für die API-Abfrage
- Ein eigener API-Key von [API Ninjas](https://api-ninjas.com/)

## Installation

1. Repository herunterladen und in den Projektordner wechseln:

   ```bash
   git clone https://github.com/Fittinator/My-Zootopia-API.git
   cd My-Zootopia-API
   ```

2. Optional eine virtuelle Python-Umgebung erstellen:

   ```bash
   python -m venv .venv
   ```

   Unter Windows PowerShell aktivieren:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   Unter macOS oder Linux aktivieren:

   ```bash
   source .venv/bin/activate
   ```

3. Benötigte Pakete installieren:

   ```bash
   python -m pip install -r requirements.txt
   ```

   Falls dein System `python3` verwendet, ersetze `python` entsprechend in den Befehlen.

## API-Key einrichten

Erstelle im Projektordner eine Datei namens `.env`. Als Vorlage kannst du `.env.example` kopieren. Trage deinen eigenen Schlüssel ein:

```ini
API_KEY='dein_api_key'
```

`python-dotenv` lädt diese Datei beim Programmstart automatisch. Bereits gesetzte Umgebungsvariablen werden dabei nicht überschrieben. Die bisherige Umgebungsvariable `API_NINJAS_KEY` wird weiterhin als Ersatz verwendet, wenn `API_KEY` leer oder nicht gesetzt ist.

Die `.env` wird durch `.gitignore` von Git ausgeschlossen. Veröffentliche deinen echten Schlüssel weder im Python-Code noch in Commits. `.env.example` enthält nur eine leere Vorlage.

## Verwendung

Starte das Programm im Projektordner:

```bash
python animals_web_generator.py
```

Beispiel:

```text
Enter a name of an animal: Fox
animals.html wurde erfolgreich erstellt!
```

Öffne anschließend `animals.html` in deinem Browser. Angezeigt werden alle Tiere, die die API für deine Suche zurückgibt. Du kannst beispielsweise auch `Monkey` eingeben. Jeder erfolgreiche Lauf ersetzt die bisherige `animals.html`.

Bei einem unbekannten Namen wie `goadohjasgfas` erzeugt das Programm eine Webseite mit einer freundlichen Meldung, dass das Tier nicht gefunden wurde. Eine leere Eingabe wird abgelehnt. Bei einem fehlenden API-Key oder einem API-Fehler erscheint eine Meldung im Terminal; die bisherige HTML-Datei bleibt erhalten.

## Projektaufbau

| Datei | Aufgabe |
| --- | --- |
| `data_fetcher.py` | Lädt die Einstellungen und ruft mit `fetch_data(animal_name)` eine Liste von Tier-Dictionaries ab. |
| `animals_web_generator.py` | Fragt nach dem Tiernamen und erstellt die HTML-Seite. |
| `animals_template.html` | Enthält das Layout und den Platzhalter für die Tierkarten. |
| `animals.html` | Die erzeugte Webseite. |
| `animals_data.json` | Frühere lokale Datenquelle; wird vom aktuellen Generator nicht verwendet. |
| `requirements.txt` | Listet `requests` und `python-dotenv` auf. |
| `.env.example` | Vorlage für die lokale Konfiguration. |

Der Data Fetcher lässt sich auch unabhängig von der Webseite verwenden:

```python
import data_fetcher

animals = data_fetcher.fetch_data("Fox")
print(f"Gefundene Tiere: {len(animals)}")
```

## Mitwirken

Verbesserungsvorschläge sind willkommen. Beschreibe Fehler oder Ideen in einem GitHub-Issue. Für Änderungen kannst du einen Fork erstellen und einen Pull Request öffnen. Prüfe vor dem Einreichen eine Suche mit Treffern und eine Suche ohne Treffer und veröffentliche keine API-Keys.
