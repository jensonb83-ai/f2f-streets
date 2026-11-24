@echo off
setlocal EnableExtensions EnableDelayedExpansion
cd /d "%~dp0"
chcp 65001 >nul
set "REPO_URL=https://github.com/jensonb83-ai/f2f-streets.git"

echo --------------------------------------------------
echo F2F Streets - Version 2.14 zu GitHub hochladen
echo Repository: %REPO_URL%
echo --------------------------------------------------
where git >nul 2>nul
if errorlevel 1 (
 echo Git wurde nicht gefunden. Bitte Git fuer Windows installieren:
 echo https://git-scm.com/downloads/win
 pause
 exit /b 1
)
if not exist .git (
 git init -b main
 if errorlevel 1 goto failed
)
git config user.name "jensonb83-ai"
git config user.email "347982756+jensonb83-ai@users.noreply.github.com"
git branch -M main

git remote get-url origin >nul 2>nul
if errorlevel 1 (
 git remote add origin "%REPO_URL%"
 if errorlevel 1 goto failed
) else (
 for /f "delims=" %%A in ('git remote get-url origin') do set "CURRENT_ORIGIN=%%A"
 if not "!CURRENT_ORIGIN!"=="%REPO_URL%" (
  echo ACHTUNG: Andere GitHub-Remote vorhanden: !CURRENT_ORIGIN!
  echo Bitte den Projektordner pruefen. Keine automatische Ueberschreibung.
  pause
  exit /b 1
 )
)

git add .
if errorlevel 1 goto failed
git diff --cached --quiet
if errorlevel 1 (
 git commit -m "F2F Streets 2.14: Online-Spiel und Downloadshop"
 if errorlevel 1 goto failed
)

echo.
echo Lade 19 Materialien, Thumbnails und die Website hoch.
echo Ggf. Anmeldung ueber den Git Credential Manager bestaetigen.
git push -u origin main
if errorlevel 1 goto failed

echo.
echo ERFOLGREICH! Repository:
echo https://github.com/jensonb83-ai/f2f-streets
start "" "https://github.com/jensonb83-ai/f2f-streets"
echo Anschliessend in Vercel das bestehende Projekt mit dem Repository verbinden.
pause
exit /b 0
:failed
echo.
echo Uebertragung nicht abgeschlossen. Bitte die Fehlermeldung oben beachten.
echo Projektdateien bleiben unveraendert im Ordner.
pause
exit /b 1
