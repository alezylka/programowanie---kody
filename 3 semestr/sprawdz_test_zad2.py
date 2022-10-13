from sprawdz_test_zad2 import kalkulator
import pytest

def test_dodawanie():
    lista1 = [2, 5, 8, 3]
    dod = 'dodawanie'
    test1 = kalkulator(dod, lista1)
    assert (test1 == 18)

def test_odejmowanie():
    lista2 = [13, 9]
    odej = 'odejmowanie'
    test2 = kalkulator(odej, lista2)
    assert (test2 == 4)

def test_mnozenie():
    lista3 = [10, 10]
    mno = 'mnozenie'
    test3 = kalkulator(mno, lista3)
    assert (test3 == 100)

def test_dzielenie():
    lista4 = [12, 2]
    dzielenie = 'dzelenie'
    test4 = kalkulator(dzielenie, lista4)
    assert (test4 == 6)