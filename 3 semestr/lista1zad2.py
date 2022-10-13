"""
@author: Aleksandra Zylka
@sources: wykład i laboratorium
"""
#1.
import pandas as pd
import matplotlib.pyplot as plt

#wczytanie danych z pliku csv do zmiennej 'health'
health = pd.read_csv('health.csv')

#wypisanie nazw chorob
print(health['disease'].unique())

#wypisanie poszczegolnych lat gdy zbierane byly dane
print('Informacje o chorobach zaczęto gromadzić w roku ' + str(health['year'].min()) + ', a zakończono w ' + str(health['year'].max()))

#wybor stanu, ktory ma sie znalezc na wykresie zarazonych
UTAH = health[health["loc"] == "UTAH"].groupby(by='disease').max()

#dzielenie wartosci z database przez 1000 w celu otrzymania procentowej wartosci zarazoncyh na wykresie
(UTAH['increase']/1000).plot.bar()
plt.xlabel("Choroba")
plt.ylabel("Procent Zarażonych ogółem")
plt.title("Procent zarażonych w Utah")
plt.show()

#2.
#wyór choroby - ospa
chosen_disease = 'SMALLPOX'

#grupowanie na podstawie choroby i lat - tworzenie histogramu z oznaczeniami
health.groupby(by=['disease', 'year']).size().loc[chosen_disease].hist()
plt.xlabel("Liczba stanów")
plt.ylabel("Wystąpienia ospy na przestrzeni lat")
plt.title("Histogram - raportowanie ospy w danych latach")
plt.show()

#3.
#tworzenie nowej kolumny w tabeli 'percent', w której znajdzie sie procentowy udział zachorowań
health.loc[:, "percent"] = health["increase"] / 1000

#Stworzenie wykresu rozwoju choroby na przestrzeni lat dla Ohio i Świnki
wykres = health.query("loc == 'OHIO' and disease == 'MUMPS'").plot(x="year", y="percent", label="Świnka w Ohio")

#Pogrupowanie tabeli poprzez chorobę i rok, sumując wszystkie wyniki. Wybranie informacji jedynie dla świnki
grupowanie = health.groupby(by=["disease", "year"]).sum().loc["MUMPS"]

#Stworzenie nowej kolumny z procentem zarażonych w danym roku
grupowanie.loc[:, "percent"] = 100 * grupowanie["number"] / grupowanie["population"]

#Wykreślenia na poprzednim wykresie nowego wykresu rozwoju choroby dla Waszyngtonu.
grupowanie.plot(y="percent", use_index=True, wykres=wykres, label="Świnka w Ameryce")

# Inne parametry wykresu
plt.legend()
plt.title("Przebieg świnki w USA")
plt.xlabel("Rok")
plt.ylabel("Procent chorującego społeczeństwa [%]")
plt.show()