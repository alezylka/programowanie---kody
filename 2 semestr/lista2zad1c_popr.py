"""
@author: Zylka Aleksandra
"""

liczba_x = 0        #szukana w tablicy liczba
powtorzenie = 0     #krotność kolejnej pętli
t = 12              #liczba elementów w tablicy T
T = [0, 3, 9, 11, 0, 19, 16, 0, 2, 2, 12, 14]   #elementy tablicy T


while powtorzenie <= (t - 1):
    if T[powtorzenie] == 0:
        liczba_x += 1
        powtorzenie += 1
    else:
        powtorzenie +=1

while powtorzenie == t:
    print('liczba szukanych elementow w tablicy:' + str(liczba_x))
    break