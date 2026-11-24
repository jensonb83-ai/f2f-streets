# F2F Streets 2.14 – GitHub & Vercel

**Repository:** https://github.com/jensonb83-ai/f2f-streets
**Produktionswebsite:** https://f2f-streets-test.vercel.app/

## 1. GitHub befüllen (einmalig)

Das Repository existiert bereits, war beim letzten Check aber noch leer. Dieses ZIP **vollständig entpacken**, sodass `index.html` und `downloads/` im selben Ordner liegen.

- **Windows:** Doppelklick auf `PUSH_NACH_GITHUB_WINDOWS.cmd` (Git für Windows muss installiert sein).
- **Mac/Linux:** Terminal im Projektordner öffnen und `bash PUSH_NACH_GITHUB_MAC_LINUX.sh` ausführen.

Das Skript überträgt die Dateien an das **bereits fest eingetragene** Repository `jensonb83-ai/f2f-streets`. Eine GitHub-Anmeldung ist bei der ersten Verwendung eventuell erforderlich. Bitte **keine Zugangstokens oder Passwörter im Chat teilen**.

**Wichtig:** Das Repository ist derzeit öffentlich. Wenn du die Testmaterialien noch nicht öffentlich zeigen möchtest, stelle unter GitHub → Settings → General → Danger Zone → Change repository visibility auf **Private** um, bevor du hochlädst. Über Vercel kann die Webseite dennoch öffentlich bleiben.

## 2. Bestehendes Vercel-Projekt verbinden

Im Vercel-Dashboard das bestehende Projekt `f2f-streets-test` öffnen (nicht versehentlich ein neues Projekt anlegen):

1. **Settings → Git** öffnen.
2. **Connect Git Repository** wählen; GitHub erlauben und `jensonb83-ai/f2f-streets` auswählen.
3. Produktionsbranch `main` einstellen. Framework `Other`, Root Directory `./`, kein Build-Befehl erforderlich.
4. Nach dem Deployment unter **Deployments** prüfen, dass das neue Deployment **Production / READY** zeigt.
5. Öffne https://f2f-streets-test.vercel.app/ und teste die Fassung 2.14 samt Materialshop.

Falls **Settings → Git** keine entsprechende Option anbietet, die Einbindung nicht erzwingen; zuerst prüfen, ob das GitHub-Repository für die Vercel-GitHub-Integration freigegeben ist.

## 3. Künftige Aktualisierungen

Nach dem ersten Upload können künftige Änderungen über denselben Projektordner hochgeladen werden (Git Commit & Push auf `main`). Vercel veröffentlicht automatisch, wenn das Repository korrekt mit dem Projekt verbunden ist.

## Datenschutz

Die Testversion hat **kein CRM oder E-Mail-Backend**. Im Downloadfenster ist eine E-Mail optional und bleibt ggf. im Browser-localStorage der jeweiligen Person.
