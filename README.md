# FeierabendTimer 🕔

Ein einfaches, lokales Web-Tool zur Berechnung deiner Arbeitszeit inkl. gesetzlicher Pausen.

## 🔧 Features

- Eingabe der Kommt-Zeit
- Automatische Berechnung des Feierabend-Zeitpunkts
- Berücksichtigung gesetzlicher Pausenregelung (ab 6h: 30min, ab 9h: 45min)
- Anzeige der verbleibenden Zeit bis zum Feierabend
- Lokale Speicherung in `arbeitszeit.csv`
- Keine zentrale Datenbank – jeder sieht nur seine Daten

## 🚀 Nutzung

1. Repository klonen:
```bash
git clone https://github.com/deinname/FeierabendTimer.git
cd FeierabendTimer
```

2. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

3. Starten:
```bash
python app.py
```

4. Seite öffnet sich im Browser – Edge bietet ggf. „Als App installieren“ an.

## 💡 Hinweis

Die Datei `arbeitszeit.csv` wird automatisch beim ersten Eintrag erstellt.
