"""
@author: Zylka Aleksandra
@sources: https://www.geeksforgeeks.org/python-program-for-binary-search/
solutions from @sherwoor and @Norah Borus:
        https://stackoverflow.com/questions/19989910/recursion-binary-search-in-python
"""

def szukanie_bin(element, tab, poczatek, koniec):
    """ Funkcja znajdujaca w tablicy metoda wyszukiwania binarnego wartosci zadane.
    Args:
        element (float): zadana wartosc, ktorej program szuka w tablicy
        tab (list): posortowana tablica
        poczatek (int): pierwszy indeks tablicy, czyli 0
        koniec (None): ostatni indeks tablicy
    Returns:
        float: pozycje/indeksy szukanej wartosci
        None: funkcja nic nie zwraca w przypadku niespelnienia warunkow poczatkowych
    """
    
    if len(tab) == 0:   #dla pustej tablicy funkcja zwraca None
        return None

    if poczatek > koniec:   #jesli w tablicy jest co najmniej 1 element
        return None
    else:
        środek = (poczatek + koniec) // 2   #okreslenie stałej środek
        if element == tab[środek]:          #jesli wartosc szukana jest w srodku zakresu przeszukiwanego
            return środek                   #program zwroci te wartosc jako indeks
        if element < tab[środek]:           #jesli wartosc szukana jest mniejsza niz element w srodku uporzadkowanej tablicy
            return szukanie_bin(element, tab, poczatek, (środek - 1))   #wowczas argumenty funkcji zmieniaja wartosci i program zapetla sie
        else:                       #jesli wart. szuk. jest wieksza niz srodkowy element tablicy
            return szukanie_bin(element, tab, (środek + 1), koniec) #argumenty funkcji zmieniaja wartosci i program zapetla sie
    

#okreslenie parametrow wejsciowych funkcji i wywolanie jej
tab = [1, 2, 3, 4, 5, 6, 7, 8, 9]
indeks = szukanie_bin(5, tab, 0, len(tab)-1)
print('Indeks szukanej wartości to: ' + str(indeks))

#Testy

#import unittest
def test_szuk_bin():
    """ Funkcja testujaca funkcje znajdujaca w tablicy wartosci
    szukane metoda binarna
    """
    wynik1 = szukanie_bin(6, [2, 4, 6, 8, 10], 0, 4)    #wprowadzenie danych wejsciowych dla funkcji testowanej jako zmienna wynik1
    assert wynik1 == 2, 'Niepoprawnie podany indeks'    #porownanie wyniku dzialania funkcji do przewidzianego wyniku
    print('Indeks szukanej wartosci to: ' + str(wynik1))    #zwrocenie komunikatu na konsoli

    wynik2 = szukanie_bin(2, [], 0, 0)
    assert wynik2 is None, 'Niepoprawnie podany indeks'
    print('Nie mozna podac indeksu szukanej liczby - brak tablicy.')

    wynik3 = szukanie_bin(0, [10, 20, 30, 40], 0, 3)
    assert wynik3 is None, 'Niepoprawnie podany indeks'
    print('Nie mozna podac indeksu szukanej liczby - nie wystepuje w tablicy.')

#wywolanie funkcji testujacej
test_szuk_bin()

