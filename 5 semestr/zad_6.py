

from sys import argv
import pandas as pd


iter = 0
f1 = 1

def z_pliku(plik):
    """
    Program wczytujacy z pliku liczby i zapisujący
    w innym pliku dane będące wynikiem operacji na nich. 
    """
    input_data = pd.read_table(plik)
    #print(input_data)      -> drukuje się DataFrame z indeksami

    
    number = int(input("Wprowadz liczbe nieparzysta"))
    iteracja = 0
    nowa_lista_1 = []
    nowa_lista_2 = []
    if number % 2 != 0:    
        for item in input_data:
            if iteracja < number:
                item = input_data.iteritems()
                nowa_lista_1.append(item)
                iteracja += 1
            for column in nowa_lista_1:
                for i in range(1, column):
                    f1,f2 = 1,1
                    i = 0
                    while i < 100:
                        f1,f2 = f2,f1+f2
                        print(f2)
                        i += 1
                    nowa_lista_2.append(f2)
    elif(number % 2 == 0):
        out = "Wprowadz liczbe nieparzysta."
    else:
        out = "Wprowadz liczbe wieksza od zera."

    out = pd.DataFrame(list(zip(nowa_lista_1, nowa_lista_2)), columns=['stare', 'nowe'])

    return out
        


z_pliku('5 semestr\odd_in.dat')