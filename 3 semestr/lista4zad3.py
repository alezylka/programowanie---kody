"""
@kod z wykładu nr 4 - rozwiązywanie nieoznaczonego
    układu równań liniowych
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#rozwiązanie układu równań dzięki modułowi algebry liniowej
A = np.matrix([[1, 2, 3],
                [0, -3, -1],
                [2, 1, 4]])

#transpozycja wekatora b
b = np.matrix([2, -5, 0]).T
#mnożenie macierzowe + inwersja (odwrócenie macierzy)
x = np.linalg.inv(A) * b

x_dokladne = np.matrix([1, 2, -1]).T
#print(x == x_dokladne)
#zwraca wartość logiczną True jeśli tablice
# są równe elementom w ramach tolerancji
print(np.allclose(x, x_dokladne))

#zastosowanie funkcji linalg.solve; rozwiązanie układu równań
#metodą lower-upper decomposition + generacja wyników w terminalu
x = np.linalg.solve(A, b)
print(x == x_dokladne)

#wizualizacja oznaczonego ukladu równań

#tworzenie wektorów punktów na osiach x1, x2
x1 = x2 = np.linspace(-3, 3, 10)
X1, X2 = np.meshgrid(x1, x2)

#tablice punktów definiujących płaszczyzny do narysowania
X3_1 = -A[0, 0]/A[0, 2] * X1 - A[0, 1]/A[0, 2] * X2 + b[0]/A[0, 2]
X3_2 = -A[1, 0]/A[1, 2] * X1 - A[1, 1]/A[1, 2] * X2 + b[1]/A[1, 2]
X3_3 = -A[2, 0]/A[2, 2] * X1 - A[2, 1]/A[2, 2] * X2 + b[2]/A[2, 2]

rys = plt.figure()

#tworzenie rysunku przy jednoczesnym pobieraniu
#odnośnika do przestrzeni 3-wymiarowej
os = rys.gca(projection='3d')

#alpha - współczynnik rozmycia
os.plot_surface(X1, X2, X3_1, alpha=0.4, color='r')
os.plot_surface(X1, X2, X3_2, alpha=0.4, color='g')
os.plot_surface(X1, X2, X3_3, alpha=0.4, color='b')

os.text(X1[0, 0], X2[0, 0], X3_1[0, 0], '$x_1$')
os.text(X1[0, 0], X2[0, 0], X3_2[0, 0], '$x_2$')
os.text(X1[0, 0], X2[0, 0], X3_3[0, 0], '$x_3$')

os.scatter(x[0, 0], x[1, 0], x[2, 0], color='k')
os.text(x[0, 0], x[1, 0], x[2, 0], '$x$')

os.set_xlabel('$x_1$')
os.set_ylabel('$x_2$')
os.set_zlabel('$x_3$')

plt.show()