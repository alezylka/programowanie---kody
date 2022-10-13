
def wygladz():
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
    pass

def szukaj_pikow():
    """Szukanie pozycji pików (ekstremów) w sygnale
        Args:
            sygnal (numpy.array): sygnał
            promien (int): promien izolacji piku (otoczenie, w którym
                            pik stanowi wartość ekstremalną)
            brzegi (bool): sposób traktowania brzegów zakresu:
                            uwzględnianie (True, wart. domyślna)
                            pomijane (False)
        Returns:
            list: lista plików
        Raises:
            ValueError: jeśli podano ujemny promień
    """ 
    pass
