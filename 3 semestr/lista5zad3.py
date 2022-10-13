import numpy as np


def wygladz(sygnal, promien):
    """Wygładzanie sygnału filtrem uśredniającym.
    
    Uwaga! Wartości na brzegach zakresu są wygładzane we fragmencie okna
    znajdującym się nad zakresem, np. dla promienia 1 (długość okna 3):
    [ 1 2 6 4 5]
    [ 1.5 ]
        [ 3 ]
            [ 4 ]
                [ 5 ]
                    [ 4.5 ]
    Args:
        sygnal (numpy.array): sygnał
        promien (int): promien uśredniania (długość okna = 2 x promien + 1)
    Returns:
        numpy.array: wygładzony sygnał
    Raises:
        ValueError: jeśli podano ujemny promień
    """
    
    zwrot = []

    for x in range(len(sygnal)):
        a = max(x - promien, 0)
        b = min(x + promien + 1, len(sygnal))
        nowy = np.mean(sygnal[a: b])
        zwrot.append(nowy)

    zwrot1 = np.array(zwrot, dtype='float_')
    return zwrot1

zakres = [1, 2, 6, 4, 5]
pr = 1
print(wygladz(zakres, pr))


def szukaj_pikow(sygnal, promien, brzegi):
    """Szukanie pozycji pików (ekstremów) w sygnale
    Args:
        sygnal (numpy.array): sygnał
        promien (int): promien izolacji piku (otoczenie, w którym
        pik stanowi wartość ekstremalną)
        brzegi (bool): sposób traktowania brzegów zakresu:
        uwzględniane (True, wartość domyślna)
        pomijane (False)
    Returns:
        list: lista pików
    Raises:
        ValueError: jeśli podano ujemny promień
    """
    pass