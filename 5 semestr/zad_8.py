
import csv
import os
import pandas as pd
from IPython.display import display

def readtable(plik):
    """
    funkcja odczytująca wartości x
    i y z tabel w sposób znormalizowany.
    Args: plik z wartościami x i y
    Returns: lista wartosci xs
            oraz lista wartosci ys
    """
    xs =[]
    ys = []
    with open(os.path.expanduser(plik), 'r') as f:
        odczyt = csv.reader(f)
        dane = list(odczyt)
        #dane = str(dane) 
        ost = [''.join(elem) for elem in dane]
        for var in ost:
            nowy = var.partition(" ")[0]
            xs.append(nowy)
            tab_xs = pd.DataFrame(xs, columns=['x'])
        
        for var in ost:
            new = var.partition(" ")[2]
            ys.append(new)
            tab_ys = pd.DataFrame(ys, columns=['y'])
        
    #return xs, ys -> powoduje, ze listy się 'sklejają"
    # i rezultat działania funkcji wygląda nieestetycznie
    print(tab_xs)
    print(tab_ys)
    print("hello:")
      
    

print(readtable('5 semestr\\x i y.csv'))


