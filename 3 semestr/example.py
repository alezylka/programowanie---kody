import pandas as pd
import matplotlib.pyplot as plt

health = pd.read_csv('health.csv')
chosen_disease = "SMALLPOX"

health.groupby(by=['disease', 'year']).size().loc[chosen_disease].hist()
plt.xlabel("Liczba stanów")
plt.ylabel("Wystąpienia chorób na przestrzeni lat")
plt.show()