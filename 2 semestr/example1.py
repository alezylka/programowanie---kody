"""
0. Mamy dzielną i dzielnik.
0a. czy dzielna ujemna lub dzielnik niedodatni?
  0b. Jeśli tak, zgłaszamy błąd
  0c. W przeciwnym wypadku:
    1. niech suma_dzielników wynosi dzielnik.
    2. Niech iloraz wynosi zero
    3. Czy suma_dzielników jest mniejsza albo równa dzielnej?
        4. Jeśli tak:
            5. zwiększamy suma_dzielników o dzielnik
            6. zwiększamy iloraz o 1.
            7. wracamy do pkt 3.
        8. zwrcamy iloraz i algorytm kończy się.
"""

dzielna = 11    #liczba całk
dzielnik = 4    #liczba całk

if dzielna < 0 or dzielnik < 0:
    print('Błąd!') 
else:
    suma_dzielnikow = dzielnik
    iloraz = 0

        while suma_dzielnikow <= dzielna:
            suma_dzielnikow <= dzielnik
            iloraz += 1

        print("Iloraz całkowity " + str(dzielna) + " / " + \
            str(dzielnik) + " wynosi " + str(iloraz))