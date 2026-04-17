"""
Grundsätzliche Erklärung eines Unit-Tests!

assert => Annahme / Behauptung
"""


def summe(a: float, b: float) -> float:
    return a + b


def test_summe():
    """Testfunktion, die summe() testet"""
    assert summe(1, 1) == 2  # Ich behaupte, dass die Summe von 1+1 = 2 ist
    assert summe(0, -1) == -1
    assert summe(2, 2) == 5


if __name__ == "__main__":
    test_summe()
