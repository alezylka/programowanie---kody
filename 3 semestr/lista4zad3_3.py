"""
@nie wiem skąd ten kod, ale działa
    można przerobić dane w pliku cos.csv
    i sprawdzić działanie dla innych danych
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#przypisanie odczytanego pliku do zmiennej table
table = pd.read_csv('cos.csv')

#utworzenie z 3 pierwszych kolumn macierzy
A = np.matrix(table.iloc[0:3, 0:3])

#"wyjęcie" z pliku kolumny b
kol_b = table["b"].values

#utworzenie z kolumny macierzy + transpozycja
b = np.matrix(kol_b).T

#mnożenie macierzowe + inwersja (odwrócenie macierzy)
x = np.linalg.inv(A) * b

print(x)

def fun(row, x, y):
    return -1 / row["a3"] * (row["a1"] * x + row["a2"] * y + row["b"])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for _, row in table.iterrows():
    #zwrot równomiernie rozmieszczonych wartości w danym przedziale
    x = y = np.arange(-3.0, 3.0, 0.05)
    #meshgrid zwraca macierze wspłrz. z wektorów wspłrz.
    X, Y = np.meshgrid(x,y)
    zs = np.array(fun(row, np.ravel(X), np.ravel(Y)))
    Z = zs.reshape(X.shape)
    ax.plot_surface(X, Y, Z)
    ax.text(X[0,0], Y[0,0], Z[0,0], '$x_1$')
    ax.scatter(x[0], x[1], x[2])
    ax.text(x[0], x[1], x[2], '$x$')
    
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$x_3$')

plt.show()


