"""
author: Zylka Aleksandra
sources: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
"""

import lista5zad1_stos as stos


def popr_rozmieszczenie(nawiasy):
    """Funkcja sprawdzajaca poprawne rozmieszczenie nawiasow okraglych w napisie
    Args:
        nawiasy(string): zmienna wejsciowa-sekwencja nawiasow okraglych do przeanalizowania
    Returns:
        True: jesli kazdemu nawiasowi otwierajacemu odpowiada nawiaz zamykajacy
        False: jesli nawiasy otwierajace i zamykajace nie tworza par
    """


    #gdy stos jest niepusty program wykonuje polecenia ponizej
    moj_stos = stos.utworz_stos()
    for element in nawiasy:
        if element == "(":
            stos.na_stos(moj_stos, element)
        elif element == ")":
            if moj_stos.wierzch is not None:
                stos.ze_stosu(moj_stos)
            else:
                return False
    if moj_stos.wierzch is None:
        return True
    else:
        return False

if __name__ == "__main__":
    napis = "a*(b*(c/(d+e)*f)"
    print(popr_rozmieszczenie(napis))


#TESTY

def test_poprawnosci():
    """Funkcja sprawdzajaca poprawnosc dzialania funkcji popr_rozmieszczenie.
    """

    string = "max(a,max(b,c))"
    sprawdzenie = popr_rozmieszczenie(string)
    assert sprawdzenie is True, 'Blednie rozmieszczone nawiasy'
    print('\n Wyrazenie ' + str(string) + ' ma poprawnie dobrane nawiasy.')

    string_1 = "6+max(a*(b/c)))"
    sprawdzenie_1 = popr_rozmieszczenie(string_1)
    assert sprawdzenie_1 is False, 'Blednie rozmieszczone nawiasy'
    print('\n Wyrazenie ' + str(string_1) + ' ma niepoprawnie dobrane nawiasy.')

    string_2 = "((c*a)/b"
    sprawdzenie_2 = popr_rozmieszczenie(string_2)
    assert sprawdzenie_2 is False, 'Blednie rozmieszczone nawiasy'
    print('\n Wyrazenie ' + str(string_2) + ' ma niepoprawnie dobrane nawiasy.')


#wywolanie funkcji
if __name__ == "__main__":
    test_poprawnosci()
