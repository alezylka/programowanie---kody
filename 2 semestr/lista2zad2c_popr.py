"""
@author: Zylka Aleksandra
"""

def liczba_elementow(t, T):
    """Obliczanie liczby wyrazen szukanych x w tablicy T.
    Args:
        t, T (float): liczba elementow t w tablicy T
        znalezionych przed konkretna iteracja
    Returns:
        float: liczba wyrazen x
        None: w przeciwnym wypadku - brak danych do zwrocenia
    """

    #dane wejsciowe do funkcji
    liczba_x = 0
    powtorzenie = 0

    if (powtorzenie > t or t == 0):
        #program zwraca ze warunki poczatkowe nie sa spelnione
        return None

    #zwrocenie liczby wyrazen x w tablicy
    while powtorzenie <= (t - 1):
        if T[powtorzenie] == 0:
            liczba_x += 1
            powtorzenie += 1
        else:
            powtorzenie +=1
    return liczba_x

print('Liczba elementow x = 0 w talicy to: ' + str(liczba_elementow(8, [3, 2, 0, 8, 4, 0, 1, 0])))   #wywolanie funkcji liczba_elementow

#Testy sprawdzajace poprawnosc dzialania funkcji liczba_elementow()

def test_liczba_x():
    """
    funkcja testujaca dzialanie funkcji liczba_elementow(t, T, powtorzenie).
    """
    liczba_x = liczba_elementow(4, [0, 2, 0, 0])
    assert liczba_x == 3, 'niepoprawnie obliczona ilosc elementow x'
    print('Liczba znalezionych elementow x = 0 to ' + str(liczba_x) + '.')

    liczba_x = liczba_elementow(0, [])
    assert liczba_x is None, 'nie sprawdzono warunkow poczatkowych danych'
    print('Wartosci danych wejsciowych nie spelniaja warunkow programu.')

print(test_liczba_x())  #wywolanie funkcji testujacej test_liczba_x
