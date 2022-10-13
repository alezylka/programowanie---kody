"""
@author: Zylka Aleksandra
@sources: https://pl.wikibooks.org/wiki/Kody_%C5%BAr%C3%B3d%C5%82owe/Algorytm_Euklidesa#Python
"""

def wspolny_dzielnik(a, b):
    """
    Funkcja znajdujaca najwiekszy wspolny dzielnik dwoch liczb dzieki algorytmowi Euklidesa
    Args:
        a, b (float) : dwie liczby calkowite, dla ktorych chce znalezc NWD.
    Returns:
        float : wartosc NWD dla podanych liczb
        None : w przypadku niewprowadzenia danych lub wprowadzenia blednych danych - brak wyjsciowej danej
    """

    if (a or b) is None:
        return None #funkcja nie zwroci zadnej wartosci, jesli nie zostanie wprowadzona jedna lub zadna z wartosci wejsciowych

    if b == 0:
        return a

    return wspolny_dzielnik(b, a % b)   #funkcja wywoluje sama siebie do momentu, gdy w wyniku dzielenia
                                        #a/b wynik będzie zerem lub ponizej zera


#wywolanie funkcji na konsolu w zdaniu
print('Najwiekszy wspolny dzielnik dla wprowadzonych liczb to: ' + str(wspolny_dzielnik(10, 5)))

#Testy

def test_nwd():
    """
    Funkcja testujaca algorytm znajdujacy najdziekszy wspolny dzielnik
    dwoch wprowadzonych liczb
    """
    test_1 = wspolny_dzielnik(9, 3) #podanie argumentow wejsciowych dla funkcji jako zmienna test_1
    assert test_1 == 3, 'niepoprawnie znaleziony NWD'   #porownanie wyniku dzialania funkcji z przewidzianym wynikiem
    print('wartosc najwiekszego wspolnego dzielnika wprowadzonych liczb to: ' + str(test_1))    #wywolanie komunikatu na konsoli

    test_2 = wspolny_dzielnik(-12, -18)
    assert test_2 == -6, 'niepoprawnie znaleziony NWD'
    print('wartosc najwiekszego wspolnego dzielnika wprowadzonych liczb to: ' + str(test_2))

    test_3 = wspolny_dzielnik(0, 3)
    assert test_3 == 3, 'niepoprawnie znaleziony NWD'
    print('wartosc najwiekszego wspolnego dzielnika wprowadzonych liczb to: ' + str(test_3))

    test_4 = wspolny_dzielnik(-1, 1)
    assert test_4 == 1, 'niepoprawnie znaleziony NWD'
    print('wartosc najwiekszego wspolnego dzielnika wprowadzonych liczb to: ' + str(test_4))

test_nwd()
#wywolanie funkcji testujacej