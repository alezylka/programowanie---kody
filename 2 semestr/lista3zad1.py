"""
@author: Zylka Aleksandra
@sources: wikibooks.org oraz sugestia przykladem podanym na zajeciach laboratoryjnych
"""

#funkcja sortujaca

def sort(tablica):
    """Sortowanie elementow tablicy w kolejnosci od najmniejszej do najwiekszej.
    Args:
        tablica (list): elementy tablicy
    Returns:
        list: tablica z przesortowanymi poprawnie elementami
        None: w przeciwnym wypadku, brak danych do zwrocenia
    """
    if len(tablica) != 0:   #jesli dlugosc tablicy jest wieksza
                            #od 0 wykonuje sie ponizsza petla
        for k in range(len(tablica) -1, 0, -1):     #dopoki ilosc iteracji zewnetrznej zawiera sie w ilosci elementow tablicy:
            for l in range(k):                      #dopoki ilosc iteracji wewnetrznych jest
                                                    #mniejsza od ilosci iteracji zewnetrznych nastepuje:
                if tablica[l] > tablica[l + 1]:     
                    tablica[l], tablica[l + 1] = tablica[l + 1], tablica[l]     #zamiana elementow miejscami
        return tablica
    else:   #jezeli w tablicy nie ma elementow, czyli jej dlugosc wynosi 0:
        return None #informacja zwrotna o braku elementow

#zdefiniowanie tablicy
tablica = [1, 5, 6, 3, 9, 0, 2, 5]
sort(tablica)   #wywolanie funkcji sortowania
print(tablica)  #drukowanie przesortowanej tablicy

#Testy

import unittest #import biblioteki
def test_sortowanie():
    """
    Funkcje testujace dla funkcji sort(tablica).
    """

    sortowanie = sort(tablica_1)
    assert sortowanie == [2, 6, 8, 12, 20], 'Niepoprawnie posortowana tablica'
    print('Poprawnie posortowana tablica wygląda następująco' + str(sortowanie) + '.')

    sortowanie = sort(tablica_2)
    assert sortowanie is None, 'Niepoprawnie posortowana tablica'
    print('Podanej tablicy nie można przesortować.')


#zdefiniowanie tablic dla testow
tablica_1 = [8, 12, 6, 2, 20]
tablica_2 = []
test_sortowanie()   #wywolanie funkcji sortowania
print(test_sortowanie)  #drukowanie przesortowanej tablicy
