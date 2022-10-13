"""
@author: Aleksandra Zylka
"""

def czesc_wspolna(Ap, Ak, Bp, Bk):
    """Obliczanie dlugosci czesci wspolnej odcinkow A i B.
    Args:
        Ap, Ak, Bp, Bk (float): polozenie punktów początkowych i koncowych
        odcinkow na osi OX
    Returns:
        float: dlugosc czesci wspolnej odcinkow pod warunkiem poprawnego
        podania polozenia poszczegolnych punktow odcinkow
        None: w przeciwnym wypadku - brak danych do zwrocenia
    """

    if not (Ap < Ak and Bp < Bk):
        #program zwraca ze warunki poczatkowe nie sa spelnione
        return None

    #zwrocenie wartosci czesci wspolnej odcinkow
    if Bp >= Ap and Bp <= Ak:
        if Bk <= Ak:
            cz_wspolna = Bk - Bp        
        else:
            cz_wspolna = Ak - Bp        
    else:
        if not(Bk < Ap and Bk > Ak):
          cz_wspolna = Bk - Ap            
        elif Bp <= Ap and Bk > Ak:
            cz_wspolna = Ak - Ap    
        else:
            cz_wspolna = 0          
    return cz_wspolna


#wartosci punktow na osi OX
czesc_wspolna(2, 7, 4, 8)
print('wartosc czesci wspolnej to: ' + str(czesc_wspolna(2, 7, 4, 8)))

#Testy

def test_czesc_wspolna():
    """
    funkcja testujaca dzialanie funkcji czesc_wspolna(Ap, Ak, Bp, Bk).
    """
    cz_wspolna = czesc_wspolna(8, -2, 2, 4)
    assert cz_wspolna is None, 'nie sprawdzono warunku na istnienie takich odcinkow'
    print('Odcinki o takich punktach krancowych nie istnieja')

    cz_wspolna = czesc_wspolna(9, 18, 7, 14)
    assert cz_wspolna == 5, 'Niepoprawnie obliczona czesc wspolna'
    print('Wartosc dlugosci czesci wspolnej odcinkow A i B o podanych punktach krancowych '\
        'wynosi ' + str(cz_wspolna) + '.')

print(test_czesc_wspolna())
