"""
@author: Kikolski
"""

import lista5zad1_stos as stos

def test_nawiasow(wyrazenie):
    """
    Funkcja sprawdzająca poprawność rozmieszczenia nawiasów w wyrażeniu algebraicznym
    Parameters
    ----------
    wyrazenie : str
        wyrażenie, które chcemy analizować
    Returns
    -------
    bool
        informacja czy wyrażenie ma prawidłowo ustawione nawiasy
    """
    s = stos.utworz_stos()
    for l in wyrazenie:
        if l == "(":
            stos.na_stos(s, l)
        elif l == ")":
            if s.wierzch is not None:
                stos.ze_stosu(s)
            else:
                return False
    if s.wierzch is None:
        return True
    else:
        return False


def test_1():
    n = "f(x)=(x^2 + (2 + x) + 3)"
    czy_poprawne = test_nawiasow(n)
    assert czy_poprawne is True, "Błędnie sprawdzone nawiasy"
    print("\n Wyrażenie " + str(n) + " ma poprawnie dobrane nawiasy")


test_1()
