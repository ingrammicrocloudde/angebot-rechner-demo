"""Mini-Bibliothek für Angebotsberechnung (Demo-Repo für GitHub Copilot).

ACHTUNG: Enthält absichtlich einen Fehler (siehe docs/ISSUES.md, Issue 1).
"""
from dataclasses import dataclass


@dataclass
class Position:
    sku: str
    menge: int
    listenpreis: float


def einzelpreis(listenpreis: float, rabatt_prozent: float) -> float:
    """Einzelpreis nach Kundenrabatt (in Prozent)."""
    # BUG: Der Rabatt wird als Absolutbetrag abgezogen statt als Prozentwert.
    return round(listenpreis - rabatt_prozent, 2)


def positionssumme(pos: Position, rabatt_prozent: float) -> float:
    return round(einzelpreis(pos.listenpreis, rabatt_prozent) * pos.menge, 2)


def angebotssumme(positionen: list[Position], rabatt_prozent: float) -> float:
    return round(sum(positionssumme(p, rabatt_prozent) for p in positionen), 2)
