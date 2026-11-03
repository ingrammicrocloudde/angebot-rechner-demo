# Issues zum Kopieren (für die Live-Demo in GitHub)

## Issue 1 – Bug: Rabatt wird falsch berechnet

**Titel:** Rabatt wird als Euro-Betrag statt als Prozent abgezogen

**Beschreibung:**
```
Beim Berechnen des Einzelpreises wird der Rabatt (z. B. 5) als Absolutbetrag abgezogen,
statt als Prozentwert. Beispiel: Listenpreis 48,50 EUR, Rabatt 5 % ergibt aktuell 43,50 EUR
statt 46,08 EUR.

Erwartet: Einzelpreis = Listenpreis * (1 - Rabatt/100), gerundet auf 2 Nachkommastellen.
Die Tests in tests/test_angebot.py schlagen aktuell fehl.
```

*Demo:* Issue einem **Copilot cloud agent** (früher Coding Agent) zuweisen (Assignee: Copilot) → er legt einen Branch und einen Pull Request mit Fix an. Alternativ im VS Code **Agent Mode**: „Behebe Issue 1 und führe die Tests aus".

## Issue 2 – Feature: Mengenstaffel

**Titel:** Mengenstaffel-Rabatt ab 50 Stück

**Beschreibung:**
```
Ab einer Positionsmenge von 50 Stück soll ein zusätzlicher Mengenrabatt von 3 % gelten,
ab 100 Stück 5 %. Der Mengenrabatt wird ZUSÄTZLICH zum Kundenrabatt gewährt (multiplikativ).

Akzeptanzkriterien:
- Neue Funktion mengenrabatt(menge) in src/angebot.py
- positionssumme berücksichtigt beide Rabatte
- Tests für Grenzwerte 49, 50, 99, 100
```

*Demo:* Zuerst nur den **Chat** fragen („Wie würdest du das umsetzen?"), dann den Agent Mode machen lassen. Diskussion: Wo muss der Mensch prüfen (Rundung, Reihenfolge der Rabatte)?

## Issue 3 – Chore: Dokumentation

**Titel:** README mit Beispiel ergänzen

*Demo:* Kurzes Beispiel für die **KI im gesamten SDLC**: Copilot schreibt die Doku aus dem Code.

---

## Weitere Copilot-Stationen (je 1–2 Minuten)

| Station | Aktion |
|---|---|
| Inline-Vervollständigung | In `angebot.py` Kommentar `# Mengenrabatt ab 50 Stück` schreiben, Tab drücken |
| Chat / Erklären | Funktion markieren → „Erkläre mir diese Funktion" |
| Tests generieren | Funktion markieren → „Schreibe Tests inkl. Grenzfälle" |
| Code Review | Pull Request → Copilot als Reviewer hinzufügen |
| Anweisungsdatei | `.github/copilot-instructions.md` zeigen: „So bringen wir Teamregeln bei" |
| Security | Tab *Security*: Dependabot, Secret Scanning, Code Scanning kurz zeigen |
