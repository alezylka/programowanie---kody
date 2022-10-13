"""
@author: Żyłka Aleksandra
@sources: stackoverflow.com
"""

#funkcja znajdujaca sekwencje RNA dla nici matrycowej DNA

def sekwencja_RNA(DNA):
    """Funkcja przyporządkowuje sekwencje RNA dla nici matrycowej DNA.
    Args:
        DNA (str): nic kodujaca DNA
    Returns:
        rev_DNA.replace...(str): znaleziona sekwencja nici RNA
        None: w przeciwnym wypadku, brak danych do zwrocenia
    """

    allowed_characters = ['A', 'C', 'G', 'T']   #zdefiniowanie rozpatrywanych przez program znakow

    if not(len(DNA) == 0):
        if any(x not in allowed_characters for x in DNA):   #jeśli w stringu zawieraja sie znaki niedozwolone
            return None
        else:
            rev_DNA = DNA[::-1]   #odczytanie tablicy DNA od tylu
            return(rev_DNA.replace('A','u').replace('T','a').replace('C','g').replace('G','c').upper()) #operacja transkrypcji DNA               
    else: #jesli string jest pusty
        return None

#zdefiniowanie danych wejsciowych
DNA = "ATCGTTGGA"
#wywolanie funkcji i wywolanie danych wyjsciowych
sekwencja_RNA(DNA)
print(sekwencja_RNA(DNA))

#Testy

import unittest
def test_sekwencja_RNA():
    """
    Funkcja sortujaca dla funkcji sekwencja(DNA)
    """

    nic_matryc = sekwencja_RNA(DNA_1)
    assert nic_matryc == 'AUAGUCCGA', 'niepoprawna sekwencja nici'
    print('Program poprawnie przyporzadkowal nic matrycowa ' + str(sekwencja_RNA(DNA_1)) + '.')

    nic_matryc = sekwencja_RNA(DNA_2)
    assert nic_matryc is None , 'niepoprawna sekwencja nici'
    print('Program niepoprawnie przyporzadkowal nic matrycowa.')

    nic_matryc = sekwencja_RNA(DNA_3)
    assert nic_matryc is None, 'niepoprawna sekwencja nici'
    print('Niepoprawnie wprowadzone dane.')

#wprowadzenie danych wejsciowych i wywolanie danych wyjsciowych
DNA_1 = "TCGGACTAT"
DNA_2 = ""
DNA_3 = "CTAAGTACK"
test_sekwencja_RNA()
print(test_sekwencja_RNA)
