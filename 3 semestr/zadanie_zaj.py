import matplotlib.pyplot as plt
import pandas as pd

table = pd.read_csv('health.csv')
#table[table["loc"] == "ALABAMA"]
ALABAMA = table.groupby(by=["loc", "year"]).mean().loc["ALABAMA",:].plt(y="population", use_index=True)
#plt.xlabel()
plt.show()
#table.groupby(by=["loc", "year"]).mean().plot()
disease = health.groupby(by=['disease', 'year']).mean().transpose().plot.bar()
ax.plot(ALABAMA,)