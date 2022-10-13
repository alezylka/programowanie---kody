"""
@author: Zylka Aleksandra
@sources: wyklad nr 5
"""

def sortowanie_szybkie_hybr(tablica, poczatek, koniec):
    """Funkcja sortujaca dlugi zakres do posortowania
    Args:
        tablica (list): tablica do posortowania
        poczatek (int): indeks tablicy, od ktorego zaczyna sie sortowanie
        koniec (int): ostatni indeks tablicy
    Returns:
        list: porostowana tablica 
    """

    #w przypadku gdy dlugosc tablicy ma mniej niz 10 elementow, sortowanie wykonuje sie algorytmem babelkowym
    if (koniec - poczatek) < 10:
        return sortow_babelkowe(tablica)
    else:   #gdy tablica ma wiecej niz 10 elementow
        if poczatek < koniec:
            osiowy = podzial(tablica, poczatek, koniec) #tworzenie zmiennej osiowy
            sortowanie_szybkie_hybr(tablica, poczatek, osiowy -1)   #funkcje wejsciowe algorytmu zmieniaja wartosci
            sortowanie_szybkie_hybr(tablica, osiowy + 1, koniec)    #na w celu porownywania do siebie kazdej kolejnej wartosci wzgledem sasiadujacej
        return tablica

def podzial(tablica, poczatek, koniec):
    """Funkcja podzialu dla sortowania szybkiego.
    Args:
        tablica (list): lista elementow do uporzadkowania
        poczatek (int): poczatek zakresu do uporzadkowania
        koniec (int): koniec zakresu do uporzadkowania
    Returns:
        int: indeks elementu osiowego
    """

    #utworzenie zmiennej na podstawie koncowego wyrazu tablicy
    wartosc_podzialu = tablica[koniec]
    i = poczatek
    #dla kazdego elementu tablicy
    for j in range(poczatek, koniec):
        if tablica[j] < wartosc_podzialu:   #gdy kolejny element tablicy jest mniejszy od koncowego
            tablica[i], tablica[j] = tablica[j], tablica[i] #sa one zamieniane miejscami
            i += 1  #po kazdej zamianie iteracja jest zwiekszana o 1
    tablica[i], tablica[koniec] = tablica[koniec], tablica[i]
    return i

def sortow_babelkowe(tablica):
    """Sortowanie elementow tablicy w kolejnosci od najmniejszej do najwiekszej.
    Args:
        tablica (list): elementy tablicy
    Returns:
        list: tablica z przesortowanymi poprawnie elementami
        None: w przeciwnym wypadku, brak danych do zwrocenia
    """

    #jesli tablica jest niepusta
    if len(tablica) != 0:           
        for k in range(len(tablica) -1, 0, -1):   #dla kazdej wartosci w zakresie tablicy  
            for l in range(k):
                if tablica[l] > tablica[l + 1]:     #jesli element tablicy jest wiekszy od kolejnego z nim
                    tablica[l], tablica[l + 1] = tablica[l + 1], tablica[l]     #sa one zamieniane miejscami w tablicy
        return tablica
    else:   #jesli tablica jest pusta, algorytm zwraca None
        return None


tablica_ex = [99, 12, 45, 2, 8, 147, 53, 60, 18, 52, 90, 33, 72, 6, 10]
sortowanie_szybkie_hybr(tablica_ex, 0, len(tablica_ex) - 1)
print('posortowana przez algorytm tablica: ' + str(tablica_ex))

def tylko_quicksort(tablica, poczatek, koniec):
    """Funkcja sortujaca dlugi zakres do posortowania
    Args:
        tablica (list): tablica do posortowania
        poczatek (int): indeks tablicy, od ktorego zaczyna sie sortowanie
        koniec (int): ostatni indeks tablicy
    Returns:
        list: porostowana tablica 
    """
    #tylko gdy tablica ma wiecej niz 10 elementow
    if poczatek < koniec:
        osiowy = podzial(tablica, poczatek, koniec) #tworzenie nowej zmiennej osiowy
        tylko_quicksort(tablica, poczatek, osiowy -1)   #zmiana paramertow wejsciowych dla kolejnego wywolania funkcji
        tylko_quicksort(tablica, osiowy + 1, koniec)
    return tablica




#Testy

def test_sortowania():
    """Funkcja testujaca dzialanie algorytmu sortujacego sortowanie_szybkie
    """
    tablica_1 = [44, 26, 18, 5, 84, 92, 32] #zdefiniowanie tablicy do testu nr 1
    test_1 = sortowanie_szybkie_hybr(tablica_1, 0, len(tablica_1) - 1)  #zdefiniowanie zmiennej test_1 jako wynik funkcji o podanych parametrach wej.
    assert test_1 == [5, 18, 26, 32, 44, 84, 92], 'Niepoprawnie posortowano tablice'    #porownanie wyniku funkcji z oczekiwanym wynikiem
    print('Poprawnie posortowana tablica: ' + str(test_1))  #wywolanie w konsoli informacji o pomyslnym przejsciu przez test

    tablica_2 = [53, 60, 18, 52, 90, 33, 72, 6, 10, 2, 144, 26, 48, 11, 421, 89, 43]
    test_2 = sortowanie_szybkie_hybr(tablica_2, 0, len(tablica_2) - 1)
    assert test_2 == [2, 6, 10, 11, 18, 26, 33, 43, 48, 52, 53, 60, 72, 89, 90, 144, 421], 'Niepoprawnie posortowano tablice'
    print('Poprawnie posortowana tablica: ' + str(test_2))

    tablica_3 = []
    test_3 = sortowanie_szybkie_hybr(tablica_3, 0, len(tablica_3) - 1)
    assert test_3 is None, 'Niepoprawnie posortowano tablice'
    print('W tablicy brak elementow - algorytm nie zadziala.')

#wywolanie funkjci do testow
test_sortowania()