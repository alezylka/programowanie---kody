
from queue import Empty
import numpy as np
from scipy.signal.filter_design import normalize
import lista5zad1
import pytest
import csv

#uruchomienie testów: wpisanie w terminalu python -m pytest

def test_normalize_simple():
    """Test funkcji normalize dla przykładowej listy wartości"""
    test1 = lista5zad1.normalize([35, 70, 105])
    oczekiwany = [0, 0.5, 1]
    assert (test1 == oczekiwany).all()


def test_normalize_inputs():
    """Test funkcji normalize - sprawdzenie złego
    typu argumentu wejściowego"""
    lista1 = [35, 60, 120]
    test2 = isinstance(lista1, list)
    assert (test2 == True)
    

def test_normalize_empty_list():
    """Test funkcji normalize - sprawdzenie złego argumentu
    - pusta lista"""
    lista2 = []
    if len(lista2) != 0:
        raise ValueError("Lista nie może być pusta")

def test_moving_average_wrong_type():
    """Test funkcji moving_average - sprawdzenie złego typu
    argumentu wejściowego"""
    x = [3, 14, 8, 96]
    test4 = isinstance(x, (list, np.ndarray))
    assert (test4 == True)

def test_moving_average_wrong_type2():
    """Test funkcji moving_average - sprawdzenie złego typu
    argumentu wejściowego 2"""
    w = 3
    test4 = isinstance(w, int)
    assert (test4 == True)

def test_moving_average_empty_list():
    """Test funkcji moving_average - sprawdzenie argumentu
    wejściowego - pusta lista"""
    lista7 = []
    if len(lista7) != 0:
        raise ValueError("Podana lista nie mże być pusta")


def test_read_ecg_signal_not_found():
    """Test funkcju read_ecg_singla - nie znaleziono pliku"""
    pass

def test_read_ecg_signal_wrong_extension():
    """Test funkcji read_ecg_singla - złe rozszerzenie pliku"""
    pass

def test_read_ecg_singal_simple():
    """Test funkcji read_ecg_signal - sprawdzenie czy wczytywane
    wartości w środku listy mają typ float"""
    pass

@pytest.fixture
def sample_ecg_signal():
    with open('sample_ecg.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            sample_ecg = line
    sample_ecg = [float(k) for k in sample_ecg]
    return sample_ecg

def test_find_r_waves_simple(sample_ecg_signal):
    """ Test funkcji test_find_r_waves_simple - sprawdzenie czy wartości
    wykrytych załamków R są w dobrym miejscu"""
    pass
    
def test_find_r_waves_equal(sample_ecg_signal):
    """ Test funkcji test_find_r_waves_simple - sprawdzenie czy zwracany
    po przefiltrowaniu sygnał ma taką samą długość
    jak sygnał podany do funkcji"""
    #lista_11 = [30, 75]
    #test_11 = lista5zad1.find_r_waves(lista_11)
    #ssert (len(lista_11) == len(test_11))
    pass