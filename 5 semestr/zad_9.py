import numpy as np
from math import e
import pandas as pd

def tabela(krok):
    """
    Funkcja drukująca tabelę
    wartości x i f(x).
    """
    list_x = []
    list_y = []
    
    for x in np.arange(-1, 1, krok):
        list_x.append(round(x, 1))
        y = e ** (-x ** 4)
        list_y.append(round(y, 5))
        
    df = pd.DataFrame(list(zip(list_x, list_y)),\
            columns = ['x', 'f(x)'])
    
    return df

print(tabela(0.1))
        
