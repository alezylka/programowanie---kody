"""
@author: Aleksandra Zylka
@sources:https://www.geeksforgeeks.org/generate-five-random-numbers-from-the-normal-distribution-using-numpy/ 
        https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/
        https://stackoverflow.com/questions/37411633/how-to-generate-a-random-normal-distribution-of-integers
"""

import numpy as np
import matplotlib.pyplot as plt



#generacja randomowych liczb z rozkładu normalnego
np.random.seed(19680801)

#okreslenie danych
mu = 100  #średnia rozkładu
sigma = 15  #odchylenie stand. rozkladu
x = mu + sigma * np.random.randn(437)

num_bins = 500  #okreslenie ilosci liczb z rozkladu normalnego

fig, ax = plt.subplots()

#histogram
n, bins, patches = ax.hist(x, num_bins, density=True)

#krzywa odpowiadajaca rozkladowi normalnemu
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '.')
ax.set_xlabel('Liczby rozkladu normalnego')
ax.set_ylabel('Wartosci')
ax.set_title(r'Histogram krzywej rozkładu normalnego')

plt.gca().legend(('krzywa rozkładu', 'wygenerowane liczby'))
#fig.tight_layout()
plt.show()