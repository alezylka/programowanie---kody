



def nastepny(elem, ile):
    """ Funkcja zwracajaca wartosc elementu oddalonego o "ile" od miejsca "elem" na liscie
    Args:
        elem(int): wartosc wejsciowa elementu, od ktorego jest liczona ilosc indeksow
        ile(int): ilosc, o jaka przesuwa sie indeks celem wskazania na element wyjsciowy
    Returns:
        elem(int): element wyjsciowy, wskazany przez wartosc "ile"
    """
    assert elem is not None and ile >= 0, 'Niewlasciwy indeks.'
    if (ile == 0):
        return elem
    else:
        elem = elem.nastepny
        return elem


