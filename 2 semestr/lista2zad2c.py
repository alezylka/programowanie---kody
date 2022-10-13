"""
@author: Aleksandra Zylka
"""

def liczba_elementow():
    """Obliczanie liczby wyrazen szukanych x w tablicy T.
    Args:
        t, T, powtorzenie (float): liczba elementow t w tablicy T
        znalezionych przed konkretna iteracja
    Returns:
        float: liczba wyrazen x
        None: w przeciwnym wypadku - brak danych do zwrocenia
    """

    #dane wejsciowe do funkcji
    liczba_x = 0
    t = 8
    T = [3, 2, 0, 8, 4, 0, 1, 0]

    if (0 > t or t == 0):
        #program zwraca ze warunki poczatkowe nie sa spelnione
        return None

    #zwrocenie liczby wyrazen x w tablicy
    if (t > 0 and 0 <= t):
        for i in T == 0:
            liczba_x += 1

    while i == t:
        print('liczba szukanych elementow w tablicy: ' + str(liczba_x))
        break

liczba_elementow()

"""
def test_liczba_x():
    
    funkcja testujaca dzialanie funkcji liczba_elementow(t, T, powtorzenie).
   

    liczba_x = 0
    t = 8
    T = [3, 2, 0, 8, 4, 0, 1, 0]
    powtorzenie = 0
    liczba_x = liczba_elementow()
    assert liczba_x == 3, 'niepoprawnie obliczona ilosc elementow x'
    print('Liczba znalezionych elementow x = 0 to' + str(liczba_x) + '.')

    liczba_x = 0
    t = 6
    T = [3, 2, 8, 4, 1,]
    powtorzenie = 0
    liczba_x = liczba_elementow()
    assert liczba_x is None, 'nie sprawdzono warunkow poczatkowych danych'
    print('wartosci danych wejsciowych nie spelniaja warunkow programu')

test_liczba_x()
"""