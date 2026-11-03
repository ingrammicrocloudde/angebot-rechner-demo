import pytest

from src.angebot import Position, angebotssumme, einzelpreis, positionssumme


def test_einzelpreis_ohne_rabatt():
    assert einzelpreis(100.0, 0) == 100.0


def test_einzelpreis_mit_rabatt_prozent():
    # 20 % auf 50 EUR = 40 EUR
    assert einzelpreis(50.0, 20) == 40.0


def test_einzelpreis_kleiner_betrag():
    # 5 % auf 48,50 EUR = 46,075 -> 46,08 (kaufmännisch gerundet)
    assert einzelpreis(48.50, 5) == pytest.approx(46.08, abs=0.01)


def test_positionssumme():
    pos = Position(sku="SN-100", menge=10, listenpreis=48.50)
    assert positionssumme(pos, 0) == 485.0


def test_angebotssumme_mit_rabatt():
    positionen = [
        Position("SN-100", 40, 48.50),
        Position("GW-210", 4, 219.00),
    ]
    # (40*48.50 + 4*219.00) * 0.95 = 2816.00 * 0.95 = 2675.20
    assert angebotssumme(positionen, 5) == pytest.approx(2675.20, abs=0.05)
