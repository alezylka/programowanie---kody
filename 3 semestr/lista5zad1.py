
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.signal import find_peaks
import os


def moving_average(x, w):
    """
    A function that calculate a movind average on signal x with a window w
    Args:
        x - original signal
        w - window
    Returns:
        filtred_signal
    Raises:
        TypeError - if types of arguments does not
        ValueError - if x is empty
    """

    if not isinstance(x, (list, np.ndarray)) or not isinstance(w, int):
        raise TypeError("Podano argumenty złego typu")
    if not len(x):
        raise ValueError("Podana lista nie może być pusta")
    return np.convolve(x, np.ones(w), 'valid') / w


def normalize(signal):
    """
    A function for normalizing a given signal to range 0-1
    Args:
        signal - a list of floats value with ecg sequence
    Returns:
        normalized_signal - signal covered to range 0-1
    Raises:
        ValueError - when an empty was given
        TypeError - when wrong type of argument was given
    """
    if not isinstance(signal, list):
        TypeError("Podany argument nie jest listą")
    if len(signal) == 0:
        ValueError("Podany sygnał musi zawierać jakieś wartości")
    min_signal = np.min(signal)
    max_signal = np.max(signal)
    normalized_signal = (signal - min_signal) / (max_signal-min_signal)
    return normalized_signal

def plot_r_waves(signal, peaks):
    """
    This function will plot a signal with a places of R waves
    Args:
        signal - a list of floats with a ecg sequence
        peaks - an x-coordinate that localize R-waves
    Returns:
        none
    Raises:
        ValueError - when an empty was given
        TypeError - when wrong type of argument was given
    """
    if not isinstance(signal, (list, np.ndarray))\
                    or not isinstance(peaks, (list, np.ndarray)):
        TypeError("Podany argument nie jest listą")
    if len(signal) == 0:
        ValueError("Podany sygnał musi zawierać jakieś wartości")
    plt.plot(peaks, signal[peaks], '*')
    plt.plot(signal)
    plt.show()

def read_ecg_signal(path):
    """
    A function for reading ecg signal from csv file
    Args:
        path - a ecg signal file path (.csv)
    Returns:
        ecg_signal
    Raises:
        FileNotFoundError - when a wrong path is provided
        TypeError - when a file does not have a csv extension
    """
    if not os.path.isfile(path):
        raise FileNotFoundError('Plik o podanej ścieżce nie istnieje')
    if not path.endswith('.csv'):
        raise TypeError('Podany plik posiada niewłaściwe rozszerzenie')
    ecg_signal = []
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            ecg_signal.append(float(line[1]))
    print(ecg_signal)
    return ecg_signal

def find_r_waves(ecg_signal):
    """
    This function will find R-waves position from the filtred ECG signal
    Args:
        ecg_signal - ecg sequence (a list of float values)
    Returns:
        ecg_filtred - normalized signal after moving average filter applied
        peaks - x-coordinated of R-wave position
    Raises:
        ValueError - when an empty was given
        TypeError - when wrong type of argument was given
    """
    if not isinstance(ecg_signal, list):
        TypeError("Podany argument nie jest listą")
    if len(ecg_signal) == 0:
        ValueError("Podany sygnał musi zawierać jakieś wartości")
    ecg_signal = normalize(ecg_signal)
    ecg_filtred = moving_average(ecg_signal, 1)
    peaks, _ = find_peaks(ecg_filtred, distance=200, height=.6)
    return ecg_filtred, peaks

#ecg_signal = read_ecg_signal('sample_ecg.csv')
#ecg_filtred, r_waves = find_r_waves(ecg_signal)
#plot_r_waves(ecg_filtred, r_waves)
