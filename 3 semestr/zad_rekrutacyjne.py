""" Zamiana słoni miejscami w sposób
zapewniający osiągnięcie oczekiwanego
przez dyrektora rezultatu przy możliwie
najmniejszym nakładzie energetycznym.

dane do zadania:
10 - liczba słoni
3015, 4728, 4802, 4361, 135, 4444, 4313, 1413, 4581, 546 - masy słoni
3, 10, 1, 8, 9, 4, 2, 7, 6, 5 - obecne ustawienie słoni
4, 9, 5, 3, 1, 6, 10, 7, 8, 2 - oczekiwane ustawienie słoni
"""

"""
czytanie danych z pliku:
f = open('nazwa_pliku', mode='b')
dane = f.read(1024*1024) # wczytujemy 1 MB danych (lub mniej, jeśli tylu już nie ma)
(...)
f.seek(0) # "przewinąć" do początku pliku (lub innej pozycji, względem początku)
(...)
pos = f.tell() # uzyskać aktualną pozycję
(...)
f.close()
"""

import itertools

for i in range(1, 10):
    obecne = [3, 10, 1, 8, 9, 4, 2, 7, 6, 5]
    permutacje = list(itertools.permutations(obecne))

#print(permutacje)



#rozkład permutacji na cykle proste
def is_valid_permutation(in_perm):
    """
    A permutation is a list of 2 lists of same size:
    a = [[1,2,3], [2,3,1]]
    means permute 1 with 2, 2 with 3, 3 with 1.
    :param in_perm: input permutation.
    """
    if not len(in_perm) == 2:
        return False
    if not len(in_perm[0]) == len(in_perm[1]):
        return False
    if not all(isinstance(n, int) for n in in_perm[0]):
        return False
    if not all(isinstance(n, int) for n in in_perm[1]):
        return False
    if not set(in_perm[0]) == set(in_perm[1]):
        return False
    return True

print(is_valid_permutation(permutacje))