"""
@author: Zylka Aleksandra
@sources: https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values?rq=1 
            https://www.python-graph-gallery.com/4-add-title-and-axis-label
            + przykład pokazany na zajęciach
"""

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

szczepionki = pd.read_csv("szczepienia.csv")

#A
#sortuje dataframe tak, aby dla kazdego kraju stan szczepien
#byl jak najbardziej aktualny

#zaczynam od grupowań po lok. i rodz. szcz.
grupowanie = szczepionki.groupby(['location', 'vaccine'])
grupowanie = grupowanie.total_vaccinations.max()
grupowanie = grupowanie.groupby('location')

#okreslam sume wszystkich wykonanych szczepien w kazdym kraju
grupowanie = grupowanie.sum('total_vaccinations')

#resetuje indeks aby w dataframe pojawily sie tytuly kolumn i indeksy
grupowanie = grupowanie.reset_index()

#sortuje malejaco wyniki
grupowanie = grupowanie.sort_values('total_vaccinations', ascending=False)

#generuje dane na wykresie

grupowanie.plot.bar(x = 'location', y = 'total_vaccinations')

#okreslam tytul wykresu i nazwy osi
plt.title('Zależność liczby szczepień od kraju')
plt.xlabel('Państwo')
plt.ylabel('Liczba szczepień')
plt.show()


"""
@sources: https://stackoverflow.com/questions/45132334/python-scatter-plot-and-matplotlib/45132457#45132457
"""

#B
#generuje z pliku tylko wiersze z krajem Poland
polska = szczepionki.loc[szczepionki['location'] == 'Poland']

#grupuje po dacie i pojedynczych dniach szczepien
polska = polska.groupby(['date', 'vaccine'])
polska = polska.total_vaccinations.max()
polska = polska.groupby('date')

#okreslam sume wszystkich wykonanych szczepien w danym dniu
polska = polska.sum('total_vaccinations')

#resetuje indeks
polska = polska.reset_index()

#sortuje wyniki po dacie od najdawniejszej
polska = polska.sort_values('date', ascending=True)

#generuje dane na wykresie

plt.scatter(polska.date, polska.total_vaccinations)

#okreslam tytul wykresu i nazwy osi
plt.title('Zależność sumy liczby szczepionek od daty')
plt.xlabel('Data')
plt.ylabel('Suma liczby szczepnień')
plt.show()


"""
@sources: https://stackoverflow.com/questions/14745022/how-to-split-a-dataframe-string-column-into-two-columns
"""
#C nie działa
#generuje z pliku tylko wiersze z krajem Poland
pl_zaszczep = szczepionki.loc[szczepionki['location'] == 'Poland']

#pfizer = pl_zaszczep.vaccine.str.extract('(?P<Pfizer/BioNTech>[A-Z ]*$)|(?P<Johnson&Johnson>[A-Z]*$)|(?P<Oxford/AstraZeneca>[A-Z]*$)|(?P<Moderna>[A-Z]*$)')
#print(pfizer)

#grupuje po dacie i pojedynczych dniach szczepien
pl_zaszczep = pl_zaszczep.groupby(['vaccine', 'total_vaccinations'])
pl_zaszczep = pl_zaszczep.total_vaccinations.max()
#pl_zaszczep = pl_zaszczep.sum('vaccine')
#pl_zaszczep = pl_zaszczep.groupby('vaccine')
#pl_zaszczep = pl_zaszczep.reset_index()

#fig, ax = plt.subplots(0,1)

#ax[0, 0].plot(pl_zaszczep.vaccine.Pfizer/BioNTech, pl_zaszczep.total_vaccinations)
#ax[0, 1].plot(pl_zaszczep.vaccine.Johnson&Johnson, pl_zaszczep.total_vaccinations)

print(pl_zaszczep)