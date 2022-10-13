"""
@author: Aleksandra Żyłka
@sources: https://docs.python.org/3/library/random.html 
"""

#importowanie bibliotek potrzebnych w programie
from random import random
import numpy
import time
import pandas as pd
import matplotlib.pyplot as plt


def quiz():
    """
    Funkcja generuje przykłady mnożenia dwóch argumentów
    i sprawdza poprawność odpowiedzi użytkownika.
    Returns:
        dframe (DataFrame): baza danych obrazująca przebieg quizu
    Variables:
        x (int): pierwszy argument mnożenia
        y (int): drugi argument mnożenia
        start_time (time): rozpoczęcie odliczania czasu odpowiedzi
        czas_obliczen (time): całkowity czas przeznaczony na obliczenie
        wynik (int): wynik działania wprowadzany do konsoli
        dzialanie (int): wynik działania obliczony przez program
                            potrzebny do sprawdzenia poprawnosci wyniku
    """
    #tworzenie pustych list, do których dodawane są zmienne otrzymane z pętli
    wynik_lista = []
    czas_lista = []
    dzialanie_lista = []

    #pętla generująca przykłady mnożenia i sprawdzająca poprawność rozwiązań
    for i in range(7):
        #losowanie argumentów
        x = round((numpy.random.uniform(low=1, high=10)), None)
        y = round((numpy.random.uniform(low=10, high=20)), None)

        #wydruk działania na konsoli
        print("Oblicz " + str(x) + "x" + str(y) + "... ")
        
        #rozpoczęcie odliczania czasu na wpisanie wyniku
        start_time = time.time()

        #dodanie poprawnie obliczonego wyniku do listy
        dzialanie = x * y
        dzialanie_lista.append(dzialanie)

        #input pojawiający się na konsoli do wprowadzenia wyniku
        #zgłaszanie wyjątku
        try:
            wynik = int(input("Podany wynik to: "))
            if wynik < 0:
                raise ValueError("Akceptowalny tylko dodatni wynik")
        except ValueError as ve:
            print(ve)

        #wprowadzenie wyniku użytkownika do listy
        wynik_lista.append(wynik)

        #pętla sprawdzająca poprawność wprowadzonego wyniku
        if wynik == dzialanie:        
            print("Poprawna odpowiedź")
        else:
            print("Odpowiedź nieprawidłowa. Poprawny wynik to " + str(x * y))
        
        #zakończenie odliczania czasu dodawania wyniku, dodanie informacji
        #o czasie do listy oraz generacja komunikatu o tym czasie na konsoli
        czas_obliczen = "%.2f sekundy" % (time.time() - start_time)
        czas_lista.append(czas_obliczen)
        print("Czas podania odpowiedzi to " + str(czas_obliczen))

    #generacja DataFrame'u i przypisanie poszczególnym danym tytułów
    dane = {'Odpowiedź użytkownika:':wynik_lista,
    'Poprawna odpowiedź:':dzialanie_lista, 'Czas:':czas_lista}
    dframe = pd.DataFrame(dane)
    print(dframe)

    #generacja wykresu punktowego zależności czasu odpowiedzi na pytania
    plt.scatter(dzialanie_lista, czas_lista)
    plt.title('Prezentacja czasu odpowiedzi na poszczególne pytania')
    plt.ylabel('Czas odpowiedzi')
    plt.xlabel('Działanie')
    plt.show()

    #zapis rezultatów w postaci tabeli do pliku .csv
    dframe.to_csv('wyniki_quiz.csv')

if __name__ == "__main__":
    quiz()







