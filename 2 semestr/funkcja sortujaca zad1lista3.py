#funkcja sortujaca
def sort(tablica):
    """Sortowanie elementow tablicy w kolejnosci od najmniejszej do najwiekszej.
    Args:
        tablica (list): elementy tablicy
    Returns:
        list: tablica z przesortowanymi poprawnie elementami
        None: w przeciwnym wypadku, brak danych do zwrocenia
    """
    
    if len(tablica) != 0:   #jesli dlugosc tablicy jest wieksza
                            #od 0 wykonuje sie ponizsza petla
        for k in range(len(tablica) -1, 0, -1):     #dopoki ilosc iteracji zewnetrznej zawiera sie w ilosci elementow tablicy:
            for l in range(k):                      #dopoki ilosc iteracji wewnetrznych jest
                                                    #mniejsza od ilosci iteracji zewnetrznych nastepuje:
                if tablica[l] > tablica[l + 1]:     #jezeli l element jest wiekszy od (l + 1)
                    tablica[l], tablica[l + 1] = tablica[l + 1], tablica[l]     #zamiana tych elementow miejscami
        return tablica
    else:   #jezeli w tablicy nie ma elementow, czyli jej dlugosc wynosi 0:
        return None #informacja zwrotna o braku elementow


tablica = [8, 5, 9, 3, 2]
sort(tablica)
print(tablica)