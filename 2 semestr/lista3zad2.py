"""
@author: Zylka Aleksandra
@sources: kod pokazany na zajeciach laboratoryjnych
"""

#funkcja potwierdzajaca lub negujaca przynaleznosc ciagu znakow do jezyka anbn

def przynaleznosc(napis):
    """Funkcja sprawdza przynaleznosc lancucha tekstu do jezyka a^2b^2
    Args:
        napis (str): napis podany przez uzytkownika
    Returns:
        Prawda (str): ciag znakow nalezy do jezyka anbn
        Fałsz: w przeciwnym wypadku, ciag nie nalezy do podanego jezyka
    """

    i = 1   #kolejna iteracja
    n = len(napis)  #okreslenie zmiennej n jako ilosci znakow w napisie
    if n == 0 or not(n % 2 == 0):   #jesli zmienna napis jest pusta lub nie jest podzielna przez 2
        return('Fałsz')
    else:
        while i in range( n // 2 ): #dopoki iteracja jest w przedziale polowy wartosc dlugosci stringu
            if napis[i] != "a" or napis[n - i - 1] != "b":  #jesli pierwsza, druga... i ostatnia, przedostatnia...//
                                                            #litera w stringu nie są odpowiednio a i b
                return('Fałsz')
            else:
                i += 1
        return('Prawda')
    
#zdefiniowanie ciagu znakow
napis = "abbb"
#wywolanie funkcji i otrzymanie informacji zwrotnej
przynaleznosc(napis)
print(przynaleznosc(napis))

#Testy

import unittest #import biblioteki
def test_przynaleznosc():
    """
    Funkcja sortujaca dla funkcji przynaleznosc(napis)
    """

    czy_nalezy = przynaleznosc(napis_1)
    assert czy_nalezy == 'Prawda', 'niepoprawnie sprawdzony ciag znakow'
    print('Podany ciag nalezy do jezyka anbn.')

    czy_nalezy = przynaleznosc(napis_2)
    assert czy_nalezy == 'Fałsz', 'niepoprawnie sprawdzony ciag znakow'
    print('Podany ciag nie nalezy do jezyka anbn.')

#wprowadzenie przez uzytkownika ciagow str
napis_1 = "ab"
napis_2 = "aabbbb"
#wywolanie funkcji oraz drukowanie danych wyjsciowych
test_przynaleznosc()
print(test_przynaleznosc)

