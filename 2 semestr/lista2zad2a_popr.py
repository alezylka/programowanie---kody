"""
@sources: materialy z zajec laboratoryjnych od Pani prowadzacej
"""
def pole_trojkata(a, b, c):
    
    """Obliczanie pola trojkata za pomoca wzoru Herona.
    Args:
        a, b, c (float): dlugosci bokow trojkata
    Returns:
        pole (float): pole trojkata pod warunkiem poprawnego podania dlugosci bokow
        None: w przeciwnym wypadku, brak danych do zwrocenia
    """

    boki = [a, b, c]

    if not (max(boki) < (sum(boki) - max(boki))):  #not a < (b + c) or b < (a + c) or c < (b + a)  
        return None

    o_pol = (a + b + c) / 2
    iloczyn = o_pol
    
    for i in range(len(boki) - 1):
        iloczyn *= o_pol - boki[i]
    pole = iloczyn**0.5
    return pole

print(pole_trojkata(3, 4, 5))


def test_pole_trojkata():
    """
    Funkcja testujaca dzialanie funkcji pole_trojkata(a, b, c).
    """
    pole = pole_trojkata(5, 5, 8)
    assert pole == 12, 'Niepoprawnie obliczone pole'
    print('Pole trojkata o podanych bokach wynosi ' + \
    str(pole) + '.')

    pole = pole_trojkata(7, 2, 12)
    assert pole is None, 'Nie sprawdzono warunku na istnienie trojkata'
    print('Trojkat o podanych bokach nie ostnieje.') 


print(test_pole_trojkata())