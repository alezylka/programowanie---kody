"""
@author: Zylka Aleksandra
@sources: wyklad 6
"""

class Stos:
    """Klasa reprezentujaca stos
    Atributes:
        wierzch(string/None (w przypadku pustego stosu)): odwolanie do wierzchu stosu
    Methods:
        utworz_stos(): utworzenie obiektu klasy stos
        na_stos(stos, napis): umieszczenie napisu na wierzchu stosu
        ze_stosu(stos): zabieranie elementu z wierzchu stosu
    """
    pass

class Element:
    """Klasa sluzaca do reprezentacji Elementu

    Attributes:
        wartosc: przypisywanie wartosci elementowi, dla ktorego wystepuje to odwolanie
        poczatek: 
        nastepny:

    Methods:
        nastepny(elem, ile):
    """
    pass

def utworz_stos():
    """Funkcja tworząca pusty stos - na jego wierzchu nie ma żadnego elementu
        
        Returns:
            stos: pusty stos (na jego wierzchu umieszczony jest None - dopiero na nim mozna "ukladac" stos)
    """
    stos = Stos()
    stos.wierzch = None
    return stos

def na_stos(stos, napis):
    """Funckcja ukladajaca elementy na stosie utowrzonym dzieki funkcji utworz_stos
        Args:
            stos(Stos(class)): pusty lub niepusty stos przyjmujacy na swoj wierzch elementy
            napis(string): element/znak jaki kladziemy na stos
        Returns:
            stos: stos, na ktorym sa elementy dodane przez funkcje
    """
    elem = Element()
    elem.wartosc = napis
    elem.poprzedni = stos.wierzch
    stos.wierzch = elem

def ze_stosu(stos):
    """Funkcja zdejmujaca z wierzchu stosu elementy
    Args:
        stos(Stos(class)): stos (może być pusty), ktory ma na sobie elementy polozone dzieki funkcji na_stos
    Returns:
        elem.wartosc(variable): stos, na ktorym nie ma juz elementow usunietych przy pomocy funkcji ze_stosu
    """
    if stos.wierzch is None:
        return None
    elem = stos.wierzch
    stos.wierzch = elem.poprzedni
    return elem.wartosc


#TESTY

def testy_stosow():
    """Funkcja testujaca funkcje na_stos i ze_stosu.
    """

    stos_testowy = utworz_stos()
    assert isinstance(stos_testowy, Stos), 'Klasa utworzonego obiektu nie wskazuje na to, ze jest stosem'
    print('\n Test klasy obiektu stos zdany.')

    stos_testowy_1 = utworz_stos()
    na_stos(stos_testowy_1, "5")
    na_stos(stos_testowy_1, "6")
    na_stos(stos_testowy_1, "9")
    element_1 = ze_stosu(stos_testowy_1)
    element_1 += ze_stosu(stos_testowy_1)
    element_1 += ze_stosu(stos_testowy_1)
    assert element_1 == '965', 'Niepoprawnie ulozony stos'
    print('\n Poprawny napis skladajacy sie z wyrazow na stosie to: ' + str(element_1))
    
    stos_testowy_2 = utworz_stos()
    na_stos(stos_testowy_2, ")")
    na_stos(stos_testowy_2, "((")
    element_2 = ze_stosu(stos_testowy_2)
    element_2 += ze_stosu(stos_testowy_2)
    assert element_2 == '(()', 'Niepoprawnie ulozony stos'
    print('\n Poprawnie ulozony stos daje napis: ' + str(element_2))

    stos_testowy_3 = utworz_stos()
    na_stos(stos_testowy_3, "345")
    na_stos(stos_testowy_3, "012")
    element_3 = ze_stosu(stos_testowy_3)
    element_3 += ze_stosu(stos_testowy_3)
    assert element_3 == '012345', 'Niepoprawnie ulozony stos'
    print('\n Poprawnie ulozony stos daje napis: ' + str(element_3))

    stos_testowy_4 = utworz_stos()
    na_stos(stos_testowy_4, "pies")
    na_stos(stos_testowy_4, "kot")
    element_4 = stos_testowy_4.wierzch.wartosc
    assert element_4 == 'kot', 'Niepoprawnie wyznaczona wartosc na wierzchu stosu'
    print('\n Test 1 atrybutu wartosc i wierzch zdany.')

    stos_testowy_5 = utworz_stos()
    na_stos(stos_testowy_5, "kruk")
    na_stos(stos_testowy_5, "lis")
    element_5 = stos_testowy_5.wierzch.wartosc
    assert element_5 == 'lis', 'Niepoprawnie wyznaczona wartosc na wierzchu stosu'
    print('\n Test 2 atrybutu wartosc i wierzch zdany.')

    stos_testowy_6 = utworz_stos()
    element_6 = ze_stosu(stos_testowy_6)
    assert element_6 is None, 'Niepoprawnie wyznaczona wartosc na wierzchu stosu'
    print('\n Brak elementow na stosie.')

#wywolanie testow

if __name__ == "__main__":
    testy_stosow()



