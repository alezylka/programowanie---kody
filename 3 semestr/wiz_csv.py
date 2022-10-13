
#WYWOŁANIE TEGO KODU:
#python wiz_csv.py nile.csv -s 2 -l

import argparse
import csv
import matplotlib.pyplot as plt

#konstrukcja biektu parsera - opis programu w odp na prośbę o pomoc
parser = argparse.ArgumentParser(description='Wizualizacja serii danych.')

#argumenty linii polecen
parser.add_argument('plik', type=str,
        help='plik z danymi w formacie csv')

#którą serię danych przetwarzamy? odp: 1 deafult'owa
parser.add_argument('-s', '--seria', type=int, default=1,
        help='numer serii danych (domyślnie: 1)')

#jaki format graficzny ma mieć wykres? 
parser.add_argument('-f', '--format', type=str,
        help='format zapisu do <plik>.<format> (opcjonalny)')

#argument uruchamiający linię zamiast punktów do rysowania wykresu
parser.add_argument('-l', '--linia', action='store_true',
        help='łączenie punktów na wykresie')

#po zbudowaniu parsera wywołanie jego funkcji składowej
args = parser.parse_args()

dane = []

#wyłapywanie wyjątków: źle sformatowanych wierszy i nienumer. danych
with open(args.plik) as plik:
    czytnik = csv.reader(plik)
    naglowek = next(czytnik)
    for wiersz in czytnik:
        try:
            dane.append(float(wiersz[args.seria - 1]))
        except:
            print("Pominięto rekord" + str(wiersz))

#rysowanie wykresu
if args.linia:
    plt.plot(dane,'-')
else:
    plt.plot(dane,'.')

plt.title(args.plik.replace('.csv', '').replace('_', ' '))
plt.ylabel(naglowek[args.seria - 1].replace('"', ''))
plt.xlabel("pozycja")

if args.format is not None:
    plt.savefig(args.plik.replace('.csv', '') + '.' + args.format)
else:
    plt.show()


