"""
@author: Zylka Aleksandra
@sources: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
"""

import lista5zad1_stos as stos
 
def stos_zbalansowany(nawiasy):
    """Funkcja sprawdzajaca czy stos ma tyle samo nawiasow otwierajacych co zamykajacych i czy sa one w poprawnej kolejnosci.

    Args:
        ciag(string): ciąg znakow nawiasow otwierajacych i zamykajacych

    Returns:
        True(logic): jesli kazdemu nawiasowi otwierajacemu odpowiada zamykajacy
        False(logic): w przeciwnym wypadku
    """

    ten_stos = stos.utworz_stos()
    for char in nawiasy:
        if char == '(':
            stos.na_stos(ten_stos, char)    
        elif char == ')':                   
            if ten_stos.wierzch is not None:
                stos.ze_stosu(ten_stos)
            else:
                return False                
        if char == '[':
            stos.na_stos(ten_stos, char)
        elif char == ']':
            if ten_stos.wierzch is not None:
                stos.ze_stosu(ten_stos)
            else:
                return False
        if char == '{':
            stos.na_stos(ten_stos, char)
        elif char == '}':
            if ten_stos.wierzch is not None:
                stos.ze_stosu(ten_stos)
            else:
                return False
    if ten_stos.wierzch is None:
        return True
    else:
        return False
 
 
#wywolanie funkcji
if __name__ == "__main__":
    nawiasy = "max{a*[b+(1/c], e/[1+f]}"
    print(stos_zbalansowany(nawiasy))

#TESTY


def test_balansu():
    """Funkcja testujaca funkcje stos_zbalansowany.
    """

    przyklad = "{(f+[a)/*3]"
    sprawdz = stos_zbalansowany(przyklad)
    assert sprawdz is False, 'Test przebiegl niepoprawnie'
    print('Podany string ma niepoprawnie dobrane nawiasy.')

    przyklad_1 = "[2+{[3/2}*4]"
    sprawdz_1 = stos_zbalansowany(przyklad_1)
    assert sprawdz_1 is False, 'Test przebiegl niepoprawnie'
    print('Podany string ma niepoprawnie dobrane nawiasy.')

    przyklad_2 = "{(a+b)/[-n]}"
    sprawdz_2 = stos_zbalansowany(przyklad_2)
    assert sprawdz_2 is True, 'Test przebiegl niepoprawnie'
    print('Podany string ma poprawnie dobrane nawiasy.')

#wywolanie funkcji
if __name__ == "__main__":
    test_balansu()