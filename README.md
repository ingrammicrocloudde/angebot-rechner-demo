# angebot-rechner (Demo-Repo)

Mini-Bibliothek zur Berechnung von Angebotspreisen. Dient als **Spielwiese für GitHub und GitHub Copilot**.

## Einrichtung des Demo-Repos auf GitHub

```bash
cd akt3-github-copilot
git init -b main
git add . && git commit -m "Initialer Stand mit bekanntem Rabatt-Bug"
gh repo create angebot-rechner-demo --private --source=. --push
```

Danach auf GitHub: Issues aus `docs/ISSUES.md` anlegen (Issue 1 und 2).

> Der CI-Lauf ist beim ersten Push **absichtlich rot** (Bug). Das ist der Ausgangspunkt der Demo.

## Lokal testen

```bash
pip install -r requirements.txt
pytest -q          # schlägt vor dem Fix fehl
```
