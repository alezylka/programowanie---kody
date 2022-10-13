
import numpy as np


t = np.arange(0, 1, 1e-3)
s = np.sin(10 * np.pi * t) + 0.1 * np.random.standard_normal(len(t))

def filtr_wygladzenie(sygnal, R):
    """Funkcja wygladzajaca sygnal s[t] oraz obliczywszy
        srednia arytmetyczna w otoczeniu punktow o promieniu R.
    Args:
        sygnal: (numpy.array): sygnał
        R (int): promien uśredniania
    Returns:
        numpy.array: wygładzony sygnał
    Raises:
        ValueError: jeśli podano ujemny promień
    """
    wygladzony = []

    for x in range(len(sygnal)):

        wygladz = (1 / ((2 * R) + 1)) * sum(s)

