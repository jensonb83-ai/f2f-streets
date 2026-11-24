# F2F Streets 2.14 auf Vercel veröffentlichen

Das ZIP entpacken. Für die Veröffentlichung ist **der Inhalt** des Ordners `f2f_streets_online_214` das Projektverzeichnis (mit `index.html`, `downloads/` und `vercel.json`). Bitte keinen darüberliegenden Ordner als Root Directory benutzen.

## Vercel CLI (bestehendes Projekt)
1. Auf dem lokalen Rechner Node.js und Vercel CLI verfügbar machen: `npm install -g vercel`
2. Im entpackten Ordner anmelden: `vercel login`
3. Projekt zuordnen: `vercel link` → bestehendes Projekt `f2f-streets-test` auswählen.
4. Vorschau hochladen: `vercel deploy`
5. Vorschau prüfen: 19 Downloadkacheln mit Bild und PDF/ZIP-Downloads, Navigation und Pop-up.
6. Erst danach veröffentlichen: `vercel deploy --prod`

Öffentliche Adresse nach erfolgreicher Veröffentlichung: https://f2f-streets-test.vercel.app/

## Datenschutz
Aktuell werden keine E-Mails an Server geschickt. Die Testadresse im Pop-up kann durch aktives Klicken lokal im Browser gespeichert werden und unter Downloads gelöscht werden. Dieser Vorgang ist kein Newsletter-Opt-in.

Ein späterer Backend-Flow ist als reine Dokumentation im Ordner `PLANUNG_Backend_spaeter` beschrieben. Kein Backend oder CRM ist aktiv.
