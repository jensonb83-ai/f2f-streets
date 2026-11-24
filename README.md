# F2F Fundraising Streets – Online-Spiel & Materialshop

Version **2.15** · statische Website mit Spiel, Charaktergalerie und kostenlosem Downloadbereich.

## Projektstruktur

- `index.html` – Online-Spiel, Galerie, FAQ, Downloadshop, Feedback-Ansicht
- `downloads/` – 19 Materialdateien (PDF, CSV, ZIP) und 19 Thumbnails
- `vercel.json` – statische Vercel-Konfiguration mit Sicherheits-Headern
- `PLANUNG_Backend_spaeter/` – nur Konzeptentwürfe; **kein aktives Backend**
- `GITHUB_VERCEL_EINRICHTEN.md` – Anleitung für den ersten GitHub-Push und Vercel-Verbindung

## Lokal testen

`index.html` im Browser öffnen. Für materialübergreifende Downloads empfiehlt sich ein lokaler Server,
zum Beispiel `python -m http.server 8000` im Projektordner und anschließend `http://localhost:8000`.

## E-Mail-Speicherung

Im Testmodus werden freiwillig eingegebene Adressen nur im jeweiligen Browser gespeichert
(`localStorage`, Schlüssel `f2f_streets_download_email_local_v1`). Es gibt **keine zentrale Übertragung**,
keine Newsletter-Anmeldung und keine aktive API.

## Hinweis zu Nutzungsrechten

Die Materialien enthalten verschiedene NGO-Namen und -Logos sowie Illustrationen.
Dieses Repository enthält **keine pauschale Open-Source-Lizenz** für diese Inhalte.
Vor einer öffentlichen Wiederverwendung ist die Rechte- und Quellenlage zu prüfen.

**Repository:** https://github.com/jensonb83-ai/f2f-streets  
**Deploy-Projekt:** f2f-streets-test auf Vercel  
**Erste Schritte:** [SCHNELLSTART_GITHUB_VERCEL.md](SCHNELLSTART_GITHUB_VERCEL.md)
