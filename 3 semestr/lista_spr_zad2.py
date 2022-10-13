"""
@SOURCES: http://math.uni.wroc.pl/~jagiella/p2python/skrypt_html/wyklad11.html#lcs_opis
"""

import numpy as np
from numpy import string_


def podciągi(napis_x, napis_y, n):
    """Funkcja znajduje w zadanych napisach wspólne podciągi
        o długości n.

    Args:
        napis_x (str): dowolny napis
        napis_y (str): dowolny napis
        n (int): długość podciągów
    Returns:
        list: lista n-gramów występujących w obu ciągach
    Raises:
        TypeError: jeśli argumenty wejściowe mają niewłaściwy typ
        ValueError: jeśli wartości n spoza zakresu
                    [1, min(len(napis_x, napis_y))]
    """

    n = len(napis_x)
    m = len(napis_y)
    cache = np.zeros((n + 1, m + 1), dtype=int)

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if napis_x[x - 1] == napis_y[y - 1]:
                cache[x, y] = 1 + cache[x - 1, y - 1]
            else:
                cache[x, y] = max(cache[x, y - 1], cache[x - 1, y])
    result = cache[n, m]
    
    solution = []
    while n > 0 and m > 0:
        if napis_x[n - 1] == napis_y[m - 1]:
            solution.append(napis_x[n - 1])
            n -= 1
            m -= 1
        elif cache[n, m] == cache[n - 1, m]:
            n -= 1
        else:
            m -= 1

    return result, ''.join(reversed(solution))
    

#wprowadzenie parametrów wejściowych i wywołanie funkcji
x = str(input('Wprowadz ciag x... '))
y = str(input('Wprowadz ciag y... '))
liczba = int(input('Wprowadz wartosc n...'))

print(podciągi(x, y, liczba))
