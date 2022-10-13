#7.2

from multiprocessing.sharedctypes import Value
import pandas as pd

sentence = "this is a rambling sentence that simply goes on and on and\
        on and just simply will not stop that is just the way things are"

#1

def liczenie(abcd):
  zliczenia = {}
  slowa = abcd.split()

  for i in slowa:
    if i in zliczenia:
      zliczenia[i] += 1
    else:
      zliczenia[i] = 1

  return zliczenia

na_tablice = liczenie(sentence)
#print(na_tablice)

print("{:<10} {:<10}".format("slowo", "liczebnosc"))

for k, v in na_tablice.items():
    zliczenia = v
    tablica = "{:<15} {:<15}".format(k, zliczenia)
    print(tablica)


tablica = pd.DataFrame(na_tablice, index=[0])
tablica_trans = tablica.T

#2 - how many words appear once, twice, thrice

trojka = 0

for val in na_tablice.values():
    if val == 3:
        trojka += 1
print("Liczba wyrazów powtorzonych trzykrotnie: ")
print(trojka)

dwojka = 0

for val in na_tablice.values():
    if val == 2:
        dwojka += 1
print("Liczba wyrazów powtorzonych dwukrotnie: ")
print(dwojka)

jedynka = 0

for val in na_tablice.values():
    if val == 1:
        jedynka += 1
print("Liczba wyrazów powtorzonych jednokrotnie: ")
print(jedynka)

#3 - total number of words in sentence equals/
# the sum of words that appears once, twice and thrice

#total numbers of words in sentence
slowa = sentence.split()
liczba_slow = len(slowa)

onc_twic_thric = 3 * trojka + 2 * dwojka + jedynka

if liczba_slow == onc_twic_thric:
    print("Liczba slow jest zgodna.")
else:
    print("Liczba slow niezgodna - sprawdz kod ponownie.")
