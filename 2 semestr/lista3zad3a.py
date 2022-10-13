"""
@author: Żyłka Aleksandra
@sources: stackoverflow.com
"""

#funkcja znajdujaca sekwencje nici matrycowej dla DNA


def sekwencja(DNA):
    """Funkcja przyporządkowuje sekwencje nici matrycowej dla DNA.
    Args:
        DNA (str): nic kodujaca DNA
    Returns:
        rev_DNA.replace... (str): znaleziona sekwencja nici matrycowej
        None: w przeciwnym wypadku, brak danych do zwrocenia
    """

    allowed_characters = ['A', 'C', 'G', 'T']      #okreslenie rozpatrywanych przez program znakow

    if not(len(DNA) == 0):  #jeśli podany string jest niepusty
        if any(x not in allowed_characters for x in DNA):   #jeśli w stringu zawieraja sie znaki niedozwolone
            return None
        else:
            rev_DNA = DNA[::-1]   #odczytanie tablicy DNA od tylu
            return(rev_DNA.replace('A','t').replace('T','a').replace('C','g').replace('G','c').upper()) #operacja transkrypcji DNA               
    else: #jesli string jest pusty
        return None

#wprowadzenie danych wejsciowych
DNA = "GCTATTAAGTGCCTC"
#wywolanie funkcji i drukowanie danych wyjsciowych
sekwencja(DNA)
print(sekwencja(DNA))

#Testy

import unittest #import biblioteki
def test_sekwencja():
    """
    Funkcja sortujaca dla funkcji sekwencja(DNA)
    """

    nic_matryc = sekwencja(DNA_1)
    assert nic_matryc == 'TCAGCCTA', 'niepoprawna sekwencja nici'
    print('Program poprawnie przyporzadkowal nic matrycowa ' + str(sekwencja(DNA_1)) + '.')

    nic_matryc = sekwencja(DNA_2)
    assert nic_matryc is None , 'niepoprawna sekwencja nici'
    print('Program niepoprawnie przyporzadkowal nic matrycowa.')

    nic_matryc = sekwencja(DNA_3)
    assert nic_matryc is None, 'niepoprawna sekwencja nici'
    print('Niepoprawnie wprowadzone dane.')

#zdefiniowanie danych wejsciowych i wywolanie danych wyjsciowych
DNA_1 = "TAGGCTGA"
DNA_2 = ""
DNA_3 = "PACGGT"
test_sekwencja()
print(test_sekwencja)

