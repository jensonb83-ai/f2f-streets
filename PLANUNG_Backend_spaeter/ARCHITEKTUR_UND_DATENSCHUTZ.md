# F2F Streets – E-Mail, Feedback, CRM / Newsletter (Planung, Stand 2.14)

**STATUS TEST:** Keine aktive Schnittstelle, keine zentrale Speicherung, keine API. Downloads bleiben frei. Die optionale E-Mail wird ausschließlich bei expliziter Nutzeraktion im localStorage des jeweiligen Browsers gespeichert. Dieser Ordner ist reine Dokumentation.

## Schritt 1: Zweck und Einwilligung
- Download jederzeit ohne E-Mail; kein Dark Pattern.
- Für Material-Updates: freiwillige, eigene Checkbox mit klarem Zweck, Datenschutzhinweis, Widerrufsmöglichkeit und Double-Opt-in bei Newsletter-Versand.
- Für reine Rückfragen: andere, eng begrenzte Zweckbindung; keine automatische Newsletter-Anmeldung.
- Keine Voreinstellung, die ein Einverständnis impliziert. Keine Rückverfolgung der Downloads auf die Identität.

## Schritt 2: Späterer technischer Flow
Browser (POST /api/interest) -> Vercel Function (Validierung, Rate-Limit, Bot-Schutz) -> gewählter Dienst (Brevo/Mailchimp oder Supabase) -> Bestätigung / ggf. Double-Opt-in.
- Serverseitige Schlüssel ausschließlich über Vercel Environment Variables; nie als Browser-JS.
- HTTPS, Datenminimierung, keine IP-Adressen als dauerhafte Datenbankfelder.
- Bei Newsletter wird erst nach bestätigtem Opt-in auf die aktive Liste geschrieben.
- Datenfelder: email, purpose, consent_at, privacy_version, source, consent_status, double_optin_at, deleted_at.
- Lösch- und Exportprozesse sowie AV-Verträge vor produktiver Aktivierung festlegen.
- Aufbewahrungs- und Datenschutzhinweise vor Livegang prüfen.

## Schritt 3: Integration und Reporting
Option A (einfach): Vercel Function -> Brevo API (Kontakt + DOI-Workflow bei Dienst). Keine zweite Datenbank erforderlich.
Option B (erweiterbar): Function -> Supabase Postgres (Interessen, Feedback und Einwilligungsnachweise) -> Brevo nur für bestätigte Kontakte.
Für Download-Statistik zunächst aggregierte, datensparsame Web-Analytics; keinen personalisierten Download-Tracker ohne separate Prüfung.

## APIs (Vorschlag)
POST /api/interest {email, purpose, consent, privacyVersion, source}
POST /api/feedback {category, message, contactEmail?}
DELETE /api/contact-request {email, proofOrVerificationToken}

## Datentabelle (Vorschlag)
contacts(id UUID, email TEXT UNIQUE, purpose TEXT, consent_status TEXT, consent_at TIMESTAMP, consent_version TEXT, source TEXT, confirmed_at TIMESTAMP NULL, deleted_at TIMESTAMP NULL)
feedback(id UUID, category TEXT, message TEXT, contact_id UUID NULL, created_at TIMESTAMP)

## Erst nach Zustimmung und Konfiguration aktivieren
- Kein Versand und keine Speicherung in dieser Testversion.
- Die API-Dateien im Ordner ENTWURF_BEISPIEL sind bewusst keine deploybaren Endpunkte.
- Dienst wählen, Datenschutz/AVV prüfen, Testkontakte verwenden, Datenlöschung testen, erst dann auf Produktion umstellen.
