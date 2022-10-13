"""
@author:
@sources:
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#HACKERRANK.COM 
"""
def argumenty(x):
    
    a = int(input("Wprowadź parametr a... "))
    b = int(input("Wprowadź parametr b... "))
    c = int(input("Wprowadź parametr c... "))
    d = int(input("Wprowadź parametr d... "))
    
    #wektor czasu oraz odpowiadający mu wektor wartości wielomianu
    funkcja = ((a * x**3) + (b * x**2) + (c * x) + d)

    return funkcja
"""

a = float(input("Wprowadź parametr a... "))
b = float(input("Wprowadź parametr b... "))
c = float(input("Wprowadź parametr c... "))
d = float(input("Wprowadź parametr d... "))

x = []
y = []

for i in range(100):
    nowa_wart = round((np.random.uniform(low=1, high=100)), None)
    x[nowa_wart] = i

for i in range(100):
    kolejna = round((np.random.uniform(low=1, high=100)), None)
    y[nowa_wart] = i


#lmbda = 3.0
pocz = 1.0
koniec = 10.0
n = 100

#u = smoothfit.fit1d(x, y, pocz, koniec, n, lmbda)
zakres = np.linspace(pocz, koniec, n)

for ola in x:
    funkcja = ((a * x^3) + (b * x^2) + (c * x) + d)
    fun = np.append(funkcja)

plt.plot(zakres, funkcja)
plt.show()

