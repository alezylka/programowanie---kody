
#1
import csv

ludzie = [['Jan', 'Kowalski', 1991],
            ['Adam', 'Zieliński', 1980],
            ['Anna', 'Wójcik', 2006]]

with open('ludzie.csv', 'w', newline='') as plik:
    skryba = csv.writer(plik, delimiter='\t')
    skryba.writerows(ludzie)

with open('ludzie.csv', 'r', newline='') as plik:
    czytnik = csv.reader(plik, delimiter='\t')
    for wiersz in czytnik:
        for element in wiersz:
            print(element, end='\t')
        print('')

#2
import pandas as pd
biometr = pd.read_csv('biometr2.tsv', delimiter='\t')
print(biometr)
pd_tab = pd.DataFrame(biometr, columns=['imię', 'płeć', 'wiek', 'waga', 'wzrost'])
#print(pd_tab)
#print(biometr.groupby(by=['Płeć']).mean())
#biometr.groupby(by=['Płeć']).mean().transpose().plot.bar()