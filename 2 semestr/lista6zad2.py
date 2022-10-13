"""
@author: Zylka Aleksandra
@sources: https://stackoverflow.com/questions/38309729/count-unique-values-with-pandas-per-groups/38309823
            https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values

"""


import pandas as pd


szczepionki = pd.read_csv("szczepienia.csv")

#A
miejsca = szczepionki.location.nunique()
print("==== Zad 2 ==== \n1. Dane zgromadzone są dla " +str(miejsca) + ' krajów.')

#B
producenci = szczepionki.vaccine.nunique()
print("2. W danych znajdują się informacje dla " +str(producenci) + " producentów szczepionek.")

#C
polska = szczepionki[szczepionki["location"] == "Poland"]
pierwszy = polska.date.min()
print("3. Najwcześniejsza data dla Polski to " + str(pierwszy))

#D
aktualne = szczepionki.date.max()
print("4. Najbardziej aktualne dane w pliku są z dnia " + str(aktualne))