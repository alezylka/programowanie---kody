"""
@author: Zylka Aleksandra
@sources: https://stackoverflow.com/questions/27466350/recursive-python-function-to-count-occurrences-of-an-element-in-a-list
"""


def zliczanie(tablica, element):
    """ Funkcja zliczajaca metoda rekursywna ilosc wystapien zadanego elementu w podanej tablicy.
    Args:
        tablica(list): tablica przeszukiwana przez program
        element(float): wartosc szukana w tablicy
    Returns:
        float: ilosc elementow znalezionych w tablicy wg kryterium algorytmu
    """

    if tablica == []:
        return 0    #funkcja zwraca brak poszukiwanych elementów jesli tablica jest pusta

    if tablica[0] == element:                       #jesli kolejne wyrazenie z tablicy jest rowne wartosci szukanego elementu
        return 1 + zliczanie(tablica[1:], element)  #program dodaje do wyniku z poprzedniej petli wartosc 1 i ponownie sie wywoluje
    else:                                           #jesli kolejne wyrazenie nie jest rowne szukanemu elementowi
        return 0 + zliczanie(tablica[1:], element)  #program nie dodaje nic do wyniku z poprzedniej petli i ponownie sie wywoluje

#wywolanie i wydruk wyniku dzialania funkcji w konsoli
zliczanie([1, 1, 3, 3, 4, 5, 6, 6, 7, 7, 8], 7)
print('Program zliczyl, ze element wystepuje w tablicy ' + str(zliczanie([1, 6, 3, 7, 8, 1, 3, 4, 5, 6, 7], 7)) + ' razy.')