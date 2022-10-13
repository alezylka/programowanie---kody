"""
@author: Zylka Aleksandra
@sources:https://pl.wikibooks.org/wiki/Kody_%C5%BAr%C3%B3d%C5%82owe/Algorytm_Euklidesa#Python
"""

#fukncja niekorzystajaca z instrukcji podstawienia
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
