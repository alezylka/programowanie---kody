"""
@author: Zylka Aleksandra
@sources: przykladowy program pokazany na zajeciach laboratoryjnych
"""
#importowanie modułu lista4zad4 i nazwanie go jako sortowanie na potrzeby
#klarownosci ponizszego algorytmu
import lista4zad4 as sortowanie

#importowanie modulu random w celu uzycia go do wygenerowania
#przykladowych tablic o zadanych zakresach
import random
lista_losowa_1 = random.sample(range(1, int(1e6)), int(1e1))
lista_losowa_2 = random.sample(range(1, int(1e6)), int(1e2))
lista_losowa_3 = random.sample(range(1, int(1e6)), int(1e3))
lista_losowa_4 = random.sample(range(1, int(1e6)), int(1e4))

#importowanie biblioteki time celem manipulowania wartosciami czasu
import time 
 

#lista losowa nr 1 - czasy dzialania programow

#przeprowadzenie sortowania babelkowego i wyznaczenie czasu dzialania programu
lista1_1 = list(lista_losowa_1)
start = time.time()
sortowanie.sortow_babelkowe(lista1_1)
czas = time.time() - start
print('sortowanie babelkowe dla listy losowej nr 1 zajmuje: {:0.7f}'.format(czas) + ' sekundy.')

#przeprowadzenie quicksort'a i wyznaczenie czasu dzialania programu
lista1_2 = list(lista_losowa_1)
start = time.time()
sortowanie.tylko_quicksort(lista1_2, 0, len(lista1_2) - 1)
czas = time.time() - start
print('quicksort dla listy losowej nr 1 zajmuje: {:0.7f}'.format(czas) + ' sekundy.')

#przeprowadzenie sortowania hybrydowego i wyznaczenie czasu dzialania programu
lista1_3 = list(lista_losowa_1)
start = time.time()
sortowanie.sortowanie_szybkie_hybr(lista1_3, 0, len(lista1_3) - 1)
czas = time.time() - start
print('sortowanie hybrydowe dla listy losowej nr 1 zajmuje: {:0.7f}'.format(czas) + ' sekundy.')

#lista losowa nr 2 - czasy dzialania programow

#przeprowadzenie sortowania babelkowego i wyznaczenie czasu dzialania programu
lista2_1 = list(lista_losowa_2)
start = time.time()
sortowanie.sortow_babelkowe(lista2_1)
czas = time.time() - start
print('sortowanie babelkowe dla listy losowej nr 2 zajmuje: {:0.7f}'.format(czas) + ' sekundy.')

#przeprowadzenie quicksort'a i wyznaczenie czasu dzialania programu
lista2_2 = list(lista_losowa_2)
start = time.time()
sortowanie.tylko_quicksort(lista2_2, 0, len(lista2_2) - 1)
czas = time.time() - start
print('quicksort dla listy losowej nr 2 zajmuje: {:0.7f}'.format(czas) + ' sekundy.')

#przeprowadzenie sortowania hybrydowego i wyznaczenie czasu dzialania programu
lista2_3 = list(lista_losowa_2)
start = time.time()
sortowanie.sortowanie_szybkie_hybr(lista2_3, 0, len(lista2_3) - 1)
czas = time.time() - start
print('sortowanie hybrydowe dla listy losowej nr 2 zajmuje: {:0.7f}'.format(czas) + ' sekundy.')

#lista losowa nr 3 - czasy dzialania programow

#przeprowadzenie sortowania babelkowego i wyznaczenie czasu dzialania programu
lista3_1 = list(lista_losowa_3)
start = time.time()
sortowanie.sortow_babelkowe(lista3_1)
czas = time.time() - start
print('sortowanie babelkowe dla listy losowej nr 3 zajmuje: {:0.7f}'.format(czas) + ' sekundy.')

#przeprowadzenie quicksort'a i wyznaczenie czasu dzialania programu
lista3_2 = list(lista_losowa_3)
start = time.time()
sortowanie.tylko_quicksort(lista3_2, 0, len(lista3_2) - 1)
czas = time.time() - start
print('quicksort dla listy losowej nr 3 zajmuje: {:0.7f}'.format(czas) + ' sekundy.')

#przeprowadzenie sortowania hybrydowego i wyznaczenie czasu dzialania programu
lista3_3 = list(lista_losowa_3)
start = time.time()
sortowanie.sortowanie_szybkie_hybr(lista3_3, 0, len(lista3_3) - 1)
czas = time.time() - start
print('sortowanie hybrydowe dla listy losowej nr 3 zajmuje: {:0.7f}'.format(czas) + ' sekundy.')

#lista losowa nr 4 - czasy dzialania programow

#przeprowadzenie sortowania babelkowego i wyznaczenie czasu dzialania programu
lista4_1 = list(lista_losowa_4)
start = time.time()
sortowanie.sortow_babelkowe(lista4_1)
czas = time.time() - start
print('sortowanie babelkowe dla listy losowej nr 4 zajmuje: {:0.7f}'.format(czas) + ' sekundy.')

#przeprowadzenie quicksort'a i wyznaczenie czasu dzialania programu
lista4_2 = list(lista_losowa_4)
start = time.time()
sortowanie.tylko_quicksort(lista4_2, 0, len(lista4_2) - 1)
czas = time.time() - start
print('quicksort dla listy losowej nr 4 zajmuje: {:0.7f}'.format(czas) + ' sekundy.')

#przeprowadzenie sortowania hybrydowego i wyznaczenie czasu dzialania programu
lista4_3 = list(lista_losowa_4)
start = time.time()
sortowanie.sortowanie_szybkie_hybr(lista4_3, 0, len(lista4_3) - 1)
czas = time.time() - start
print('sortowanie hybrydowe dla listy losowej nr 4 zajmuje: {:0.7f}'.format(czas) + ' sekundy.')

