"""
@author: Zylka Aleksandra
@sources: https://stackabuse.com/python-get-number-of-elements-in-a-list/ ;
            https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
"""


class Element:
    """Klasa sluzaca do reprezentacji Elementu

    Attributes:
        wartosc: atrybut odwolujacy sie do wartosci elementu
        nastepny: atrybut odwolujacy sie do nastepnego (po wskazanym) elementu listy

    Methods:
        nastepny(elem, ile): zwraca wartosc o "ile" polozona od wartosci "elem"
    """
    pass

class Lista:
    """Klasa sluzaca do reprezentacji Listy

    Attributes:
        poczatek: atrybut odwolujacy sie do pierwszego elementu listy
        koniec: atrybut odwolujacy sie do ostatniego elementu listy

    Methods:
        utworz_liste(): towrzy obiekt klasy Lista
        dopisz(lista, napis): dodaje do listy element
        zwroc(lista, ktory): zwraca wartość z listy tej wielkosci, ktorej indeks podamy
        zmien(lista, ktory, napis): zmienia w liscie wartosc elementu, ktorego indeks podamy
        wstaw(lista, ktory, napis): wstawia do listy element w miejsce, ktorego indeks podamy
        usun(lista, ktory): usuwa z listy element o indeksie ktory podamy
    """
    pass


def utworz_liste():
    """ Funkcja tworzaca liste, na ktorej pozniej pracuja ponizsze funkcje.
    Returns:
        lista(object): pusta lista, znajduje sie w niej None
    """
    lista = Lista()
    lista.poczatek = None
    return lista


def dopisz(lista, napis):
    """ Funkcja dopisujaca na koniec listy element liczbowy lub string.
    Args:
        lista(object): pusta lub niepusta lista, ktoa jest obiektem operacji
        napis(Any): okreslony napis dopisywany na koncu listy przez funkcje
    """
    elem = Element()
    elem.wartosc = napis
    elem.nastepny = None
    if lista.poczatek is None:
        lista.poczatek = elem
    else:
        pomocniczy = lista.poczatek
        while pomocniczy.nastepny is not None:
            pomocniczy = pomocniczy.nastepny
        pomocniczy.nastepny = elem


moja_lista = utworz_liste()
dopisz(moja_lista, "Ala")
dopisz(moja_lista, "ma")
dopisz(moja_lista, "kota.")

elem = moja_lista.poczatek
while elem is not None:
    print(elem.wartosc, end = ' ')
    elem = elem.nastepny



def nastepny(elem, ile):
    """Funkcja rekurencyjna zwracajaca wartosc elementu oddalonego o "ile" od miejsca "elem" na liscie
    Args:
        elem(object): wartosc wejsciowa elementu, od ktorego jest liczona ilosc indeksow
        ile(int): ilosc, o jaka przesuwa sie indeks celem wskazania na element wyjsciowy
    Returns:
        elem(object): element wyjsciowy, wskazany przez funkcje
    """
    assert elem is not None and ile >= 0, 'Niewlasciwy indeks.'
    if (ile == 0):
        return elem
    return nastepny(elem.nastepny, ile - 1)


#podpunkt b)

def nastepny_iteracyjnie(elem, ile):
    """ Funkcja zwracajaca wartosc (w sposob iteracyjny) elementu oddalonego o "ile" od miejsca "elem" na liscie
    Args:
        elem(object): wartosc wejsciowa elementu, od ktorego jest liczona ilosc indeksow
        ile(int): ilosc, o jaka przesuwa sie indeks celem wskazania na element wyjsciowy
    Returns:
        elem(object): element wyjsciowy, wskazany przez funkcje
    """
    assert elem is not None and ile >= 0, 'Niewlasciwy indeks.'
    for n in range(ile):
        elem = elem.nastepny
        return elem

#podpunkt c)

def dlugosc(lista):
    """Funkcja zwracajaca dlugosc listy.
    Args:
        lista(object): wprowadzona lista, ktora jest przeszukiwana przez funkcje
    Returns:
        n(int): dlugosc listy
    """
    n = 0
    for element in lista:
        n += 1
    return n


#podpunkt d)

def znajdz(lista, wartosc):
    """ Funkcja podajaca indeks elementu o zadanej wartosci, jesli znajduje sie na liscie.
    Args:
        lista(object): wprowadzona lista przeszukiwana przez funkcje
        wartosc(Any): wartosc, ktora ma byc znaleziona w liscie
    Returns:
        ind(int): indeks wartosci, ktora znalazla funkcja
        None: gdy nie znaleziono szukanej wartosci w liscie
    """
    if wartosc in lista:
        return lista.index(wartosc)
    else:
        return None



def zwroc(lista, ktory):
    """ Funkcja zwracajaca wartosc elementu wskazanego przez indeks o wartosci "ktory" na liscie.
    Args:
        lista(object): lista przeszukiwana przez funkcje
        ktory(int): indeks szukanego przez funkcje elementu
    Returns:
        elem.wartosc(Any): wartosc elementu, ktora wskazal indeks
    """
    elem = nastepny(lista.poczatek, ktory)
    return elem.wartosc


def zmien(lista, ktory, napis):
    """ Funkcja zmieniajaca wartosc elementu na liscie wskazanego przez indeks na wartosc wprowadzona.
    Args:
        lista(object): lista modyfikowana przez funkcje
        ktory(int): indeks elementu, ktory ma byc zmodyfikowany
        napis(Any): element wstawiany w liste w miejscu wskazanym przez wprowadzony indeks
    """
    elem = nastepny(lista.poczatek, ktory)
    elem.wartosc = napis


def wstaw(lista, ktory, napis):
    """ Funkcja wstawiajaca na liscie napis w miejscu okreslonym w zmiennych wejsciowych.
    Args:
        lista(object): lista modyfikowana przez funkcje
        ktory(int): wartosc indeksu elementu, czyli miejsce w ktore ma byc wstawiony napis
        napis(Any): element wstawiany w liste w miejscu wskazanym przez wprowadzony indeks
    """
    elem = Element()
    elem.wartosc = napis
    if ktory == 0:
        elem.nastepny = lista.poczatek
        lista.poczatek = elem
    else:
        elem_poprz = nastepny(lista.poczatek, ktory - 1)
        elem.nastepny = elem_poprz.nastepny
        elem_poprz.nastepny = elem


def usun(lista, ktory):
    """ Funkcja usuwajaca z listy element, ktorego indeks wprowadzony jest w zmiennej "ktory".
    Args:
        lista(object): lista modyfikowana przez funkcje
        ktory(int): wartosc indeksu elementu, czyli miejsce w ktore ma byc wstawiony napis
    """
    if ktory == 0 and lista.poczatek is not None:
        lista.poczatek = lista.poczatek.nastepny
    else:
        elem_poprz = nastepny(lista.poczatek, ktory - 1)
        elem_poprz.nastepny = elem_poprz.nastepny.nastepny
        

zmien(moja_lista, 0, "Ala")
usun(moja_lista, 1)
wstaw(moja_lista, 1, "goni")
usun(moja_lista, 2)
wstaw(moja_lista, 2, "psa.")
wstaw(moja_lista, 0, "Kaczka")

elem = moja_lista.poczatek
while elem is not None:
    print(elem.wartosc, end = ' ')
    elem = elem.nastepny



#TESTY

def test_listy():
    """Funkcja testujaca funkcje z tego modułu.
    """

    lista_testowa = utworz_liste()
    assert isinstance(lista_testowa, Lista), 'Klasa utworzonego obiektu nie wskazuje na to, ze jest lista'
    print('\n Test klasy obiektu lista zdany.')


def test_dopisz():
    """Funkcja testujaca funkcje z tego modułu.
    """

    lista_testowa_1 = utworz_liste()
    przyklad = "Ala ma"
    dopisz(lista_testowa_1, przyklad)
    przyklad = " kota."
    dopisz(lista_testowa_1, przyklad)
    przyklad = lista_testowa_1.poczatek
    test = ''
    while przyklad is not None:
        test += przyklad.wartosc
        przyklad = przyklad.nastepny
    assert test == 'Ala ma kota.', 'Niepoprawnie uzupelniona lista'
    print('\n Poprawnie uzupelniona lista zawiera w sobie elementy: ' + str(test))
    
    lista_testowa_2 = utworz_liste()
    np = "1"
    dopisz(lista_testowa_2, np)
    np = "3"
    dopisz(lista_testowa_2, np)
    np = "5"
    dopisz(lista_testowa_2, np)
    np = lista_testowa_2.poczatek
    test = ''
    while np is not None:
        test += np.wartosc
        np = np.nastepny
    assert test == "135", 'Niepoprawnie uzupelniona lista'
    print('\n Poprawnie uzupelniona lista zawiera w sobie elementy: ' + str(test))

    lista_testowa_3 = utworz_liste()
    kolejny = "google"
    dopisz(lista_testowa_3, kolejny)
    kolejny = " microsoft"
    dopisz(lista_testowa_3, kolejny)
    kolejny = lista_testowa_3.poczatek
    test = ''
    while kolejny is not None:
        test += kolejny.wartosc
        kolejny = kolejny.nastepny
    assert test == "google microsoft", 'Niepoprawnie uzupelniona lista'
    print('\n Poprawnie uzupelniona lista zawiera w sobie elementy: ' + str(test))

    


def test_zwrotu():
    """Funkcja sprawdzajaca dzialanie funkcji zwroc.
    """
    lista_testowa = utworz_liste()
    dopisz(lista_testowa, "Ogniem")
    dopisz(lista_testowa, "i")
    dopisz(lista_testowa, "mieczem")
    elem_test = zwroc(lista_testowa, 2)
    assert elem_test == "mieczem", 'Zwrocono zla wartosc'
    print('\n Element o indeksie 2 ma wartosc: ' + str(elem_test))
    
    lista_testowa_2 = utworz_liste()
    dopisz(lista_testowa_2, "sklep")
    dopisz(lista_testowa_2, "z")
    dopisz(lista_testowa_2, "pomidorami")
    elem_test2 = zwroc(lista_testowa_2, 0)
    assert elem_test2 == "sklep", 'Zwrocono zla wartosc'
    print('\n Element o indeksie 3 ma wartosc: ' + str(elem_test2))

    lista_testowa_3 = utworz_liste()
    dopisz(lista_testowa_3, "5")
    dopisz(lista_testowa_3, "10")
    dopisz(lista_testowa_3, "15")
    dopisz(lista_testowa_3, "20")
    dopisz(lista_testowa_3, "25")
    elem_test3 = zwroc(lista_testowa_3, 3)
    assert elem_test3 == "20", 'Zwrocono zla wartosc'
    print('\n Element o indeksie 3 ma wartosc: ' + str(elem_test3))




def test_dlugosci():
    """Funkcja sprawdzajaca poprawnosc funkcji dlugosc.
    """
    pory_roku = ["styczeń", "luty", "marzec", "kwiecien"]
    testowy = dlugosc(pory_roku)
    assert testowy == 4, 'Zwrocono zla wartosc'
    print('\n Liczba miesiecy podanych w liscie pory_roku wynosi: ' + str(dlugosc(pory_roku)))

    zwierzeta = ["pies", "kot", "mysz", "kaczka", "kon", "kura"]
    testowy = dlugosc(zwierzeta)
    assert testowy == 6, 'Zwrocono zla wartosc'
    print('\n Wymieniono ' + str(dlugosc(zwierzeta)) + ' rodzajow zwierzat.')

    kapcie = ["lewy", "prawy"]
    testowy = dlugosc(kapcie)
    assert testowy == 2, 'Zwrocono zla wartosc'
    print('\n Para to ' + str(dlugosc(kapcie)) + ' kapcie.')


def test_znajdz():
    """Funkcja sprawdzajaca poprawnosc dzialania funkcji znajdz.
    """

    szukana = 3
    lista_elementow = [2, 4, 6, 8, 1, 3, 5, 7, 9]
    testowy = znajdz(lista_elementow, szukana)
    assert testowy == 5, 'Zwrocono zla wartosc'
    print('\n Indeks szukanej liczby na liscie elementow to: ' + str(znajdz(lista_elementow, szukana)))

    szukana_2 = 7
    lista_elementow_2 = [2, 4, 5, 9]
    testowy = znajdz(lista_elementow_2, szukana_2)
    assert testowy is None, 'Zwrocono zla wartosc'
    print('\n Indeks szukanej liczby na liscie elementow to: ' + str(znajdz(lista_elementow_2, szukana_2)))

    szukana_3 = "pies"
    lista_elementow_3 = ["pies", "kot", "mysz", "kaczka", "kon", "kura"]
    testowy = znajdz(lista_elementow_3, szukana_3)
    assert testowy == 0, 'Zwrocono zla wartosc'
    print('\n Indeks szukanej liczby na liscie elementow to: ' + str(znajdz(lista_elementow_3, szukana_3)))


def test_wstaw():
    """Funkcja sprawdzajaca poprawnosc dzialania funkcji wstaw.
    """

    ta_lista = utworz_liste()          #["nie", "ma", "sera"]
    dopisz(ta_lista, "nie")
    dopisz(ta_lista, "ma")
    dopisz(ta_lista, "sera")
    wstaw(ta_lista, 2, "mleka")
    test = zwroc(ta_lista, 2)
    assert test == "mleka", 'Funkcja zadzialala blednie'
    print('\n Poprawnie uzupelniona lista o slowo: ' + str(test))

    ta_lista_2 = utworz_liste()
    dopisz(ta_lista_2, "5")
    dopisz(ta_lista_2, "8")
    dopisz(ta_lista_2, "10")
    wstaw(ta_lista_2, 1, "7")
    test = zwroc(ta_lista_2, 1)
    assert test == "7", 'Funkcja zadzialala blednie'
    print('\n Poprawnie uzupelniona lista o slowo: ' + str(test))

    ta_lista_3 = utworz_liste()
    dopisz(ta_lista_3, "99")
    dopisz(ta_lista_3, "108")
    dopisz(ta_lista_3, "pszczola")
    dopisz(ta_lista_3, "1001")
    wstaw(ta_lista_3, 2, "mak")
    test = zwroc(ta_lista_3, 2)
    assert test == "mak", 'Funkcja zadzialala blednie'
    print('\n Poprawnie uzupelniona lista o slowo: ' + str(test))



def test_zmien():
    """Funkcja sprawdzajaca poprawnosc dzialania funkcji zmien.
    """

    lista_elementow = utworz_liste()      #["pies", "kot", "mysz", "kaczka", "kon", "kura"]
    dopisz(lista_elementow, "pies")
    dopisz(lista_elementow, "kot")
    dopisz(lista_elementow, "mysz")
    dopisz(lista_elementow, "kura")
    dopisz(lista_elementow, "kon")
    zmien(lista_elementow, 2, "5")
    test = zwroc(lista_elementow, 2)
    assert test == "5", 'Funkcja zadzialala blednie'
    print('\n Poprawnie wygenerowana lista to: ' + str(test))

    lista_elementow_2 = utworz_liste()         #["1", "2", "3"]
    dopisz(lista_elementow_2, "1")
    dopisz(lista_elementow_2, "3")
    dopisz(lista_elementow_2, "5")
    dopisz(lista_elementow_2, "20")
    dopisz(lista_elementow_2, "40")
    zmien(lista_elementow_2, 1, "20")
    test2 = zwroc(lista_elementow_2, 1)
    assert test2 == "20", 'Funkcja zadzialala blednie'
    print('\n Poprawnie wygenerowana lista to: ' + str(test2))

    lista_elementow_3 = utworz_liste()        #["4", "8", "12"]
    dopisz(lista_elementow_3, "4")
    dopisz(lista_elementow_3, "8")
    dopisz(lista_elementow_3, "12")
    zmien(lista_elementow_3, 0, "63")
    test3 = zwroc(lista_elementow_3, 0)
    assert test3 == "63", 'Funkcja zadzialala blednie'
    print('\n Poprawnie wygenerowana lista to: ' + str(test3))



def test_usun():
    """Funkcja sprawdzajaca poprawnosc dzialania funkcji usun.
    """

    lista_elementow = utworz_liste()
    dopisz(lista_elementow, "pies")
    dopisz(lista_elementow, "kot")
    dopisz(lista_elementow, "mysz")
    dopisz(lista_elementow, "kura")
    dopisz(lista_elementow, "kon")
    usun(lista_elementow, 2)
    test = zwroc(lista_elementow, 2)
    assert test == "kura", 'Funkcja zadzialala blednie'
    print('\n Poprawnie zastapiono usuniety wyraz elementem: ' + str(test))

    lista_elementow_2 = utworz_liste()
    dopisz(lista_elementow_2, "99")
    dopisz(lista_elementow_2, "108")
    dopisz(lista_elementow_2, "pszczola")
    dopisz(lista_elementow_2, "1001")
    usun(lista_elementow_2, 1)
    test = zwroc(lista_elementow_2, 1)
    assert test == "pszczola", 'Funkcja zadzialala blednie'
    print('\n Poprawnie zastapiono usuniety wyraz elementem: ' + str(test))

    pory_roku = utworz_liste()
    dopisz(pory_roku, "maj")
    dopisz(pory_roku, "czerwiec")
    dopisz(pory_roku, "lipiec")
    usun(pory_roku, 0)
    test = zwroc(pory_roku, 0)
    assert test == "czerwiec", 'Funkcja zadzialala blednie'
    print('\n Poprawnie zastapiono usuniety wyraz elementem: ' + str(test))



if __name__ == "__main__":
    test_listy()
    test_dopisz()
    test_zwrotu()
    test_dlugosci()
    test_znajdz()
    test_wstaw()
    test_zmien()
    test_usun()