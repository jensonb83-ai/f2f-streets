# Einmaliges Einrichten: GitHub → bestehendes Vercel-Projekt

## 1. Neues GitHub-Repository erstellen

1. Gehe zu https://github.com/new und melde dich im verbundenen GitHub-Konto an.
2. Repository-Name: `f2f-streets`.
3. **Private** ist für die Testphase empfohlen. Die Vercel-Webseite kann trotzdem öffentlich sein.
4. **Kein** README, keine `.gitignore` und keine Lizenz automatisch anlegen (alles im Paket vorhanden).
5. `Create repository` auswählen.
6. Kopiere auf der leeren Repository-Seite die HTTPS-URL, z. B. `https://github.com/DEIN-ACCOUNT/f2f-streets.git`.

Warum Git statt Browser-Upload? Einige Spiel-PDFs und ZIPs sind größer als
GitHubs 25-MiB-Beschränkung beim Hochladen über die Weboberfläche.
Über Git selbst sind Dateien unter 100 MiB möglich.

## 2. Projekt in das Repository hochladen

### Windows

- Git installieren: https://git-scm.com/downloads/win
- Den ganzen Projektordner entpacken und die Datei
  `PUSH_NACH_GITHUB_WINDOWS.cmd` darin starten.
- Die HTTPS-URL des zuvor erstellten GitHub-Repositories eingeben.
- Ggf. über den Git Credential Manager bei GitHub anmelden.

### macOS / Linux

Im entpackten Projektordner:

```sh
git init -b main
git add .
git -c user.name="F2F Streets" -c user.email="f2f-streets@users.noreply.github.com" commit -m "Initial release F2F Streets 2.14"
git remote add origin https://github.com/DEIN-ACCOUNT/f2f-streets.git
git push -u origin main
```

Hinweis: Die GitHub-Anmeldung erfolgt über den lokalen Git-Client; Passwörter oder Tokens
niemals in Chatnachrichten einfügen.

## 3. Bestehendes Vercel-Projekt mit GitHub verknüpfen

1. Melde dich bei https://vercel.com/dashboard an.
2. Öffne das **bestehende** Projekt `f2f-streets-test`
   (nicht aus Versehen ein neues Projekt mit neuem Namen erzeugen).
3. Unter **Settings → Git** die Option zum Verbinden eines Git-Repositories auswählen.
4. GitHub autorisieren und das Repository `f2f-streets` auswählen.
5. Produktionsbranch `main`, Root Directory `./` beziehungsweise leer, Framework **Other/None**;
   kein Build-Befehl nötig.
6. Deployment nach dem Push abwarten und anhand der Deployment-ID prüfen,
   ob die Produktion die neue Version 2.14 zeigt.

Das bestehende Produktionsziel ist `https://f2f-streets-test.vercel.app/`.
Falls Vercel die Verknüpfung eines bestehenden Projekts nicht anbietet,
nicht ungeprüft die Domain auf ein anderes Projekt zeigen lassen;
zuerst Projekt-Einstellungen prüfen.

## 4. Öffentlichen Test prüfen

- Versionshinweis: **2.14**
- 19 Downloadangebote und 19 Vorschaubilder
- Testdownloads: PDF, ZIP und CSV
- Filter/Suche
- Die E-Mail im Pop-up wird nicht an einen Server übertragen
- Spielstart, Joker, Impro-Sperre und Punktewertung

## Spätere Updates

Nach der ersten Einrichtung genügt lokal:

```sh
git add .
git commit -m "F2F Streets: Inhalte aktualisiert"
git push
```

Vercel baut die neue Version automatisch aus dem `main`-Branch.
