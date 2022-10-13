"""
@author: Zylka Aleksandra
@sorces: https://pythonexamples.org/pandas-dataframe-shape/
        https://stackoverflow.com/questions/15891038/change-column-type-in-pandas 
"""

#A
from numpy import datetime64
import pandas as pd


szczepionki = pd.read_csv("szczepienia.csv")

#B
print("==== Zad 1 ==== \nDataFrame ma " + str(szczepionki.shape[0]) + " wierszy i " + str(szczepionki.shape[1]) + " kolumny.")

#C
print(szczepionki.dtypes)

#D
szczepionki = szczepionki.astype({"location": 'string'})
szczepionki = szczepionki.astype({"date": datetime64})
szczepionki = szczepionki.astype({"vaccine": 'string'})
print(szczepionki.dtypes)

