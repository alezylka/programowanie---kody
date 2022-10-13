
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import convolve
import nrrd



plik = 'foolc.nrrd'
obraz, naglowek = nrrd.read(plik)

rys, osie = plt.subplots(ncols=5, nrows=2, constrained_layout=True)
i = 0


filtr1 = np.array([[ 0, 0, 0],
                [0, 0, 0],
                [ 0, 0, 1/4]])


def konwo(przekroj, filtr):
    wyostrzony = np.array(przekroj)
    for x in range(0, przekroj.shape[0] - filtr.shape[0] + 1):
        for y in range(0, przekroj.shape[1] - filtr.shape[1] + 1):
            wyostrzony[x+1, y+1] = np.sum(przekroj[x:x+filtr.shape[0],
                                            y:y+filtr.shape[1]]
                                            * filtr)
    return wyostrzony

for os in osie.flatten():
    #w przypadku niektórych grafik zamiast obraz[i, :, :]
    #należy filtrować obraz[i, :, None]
    wyostrzony = convolve(obraz[i, :, :], filtr1)
    os.imshow(wyostrzony, cmap=plt.cm.gray)
    os.set_xticks([])
    os.set_yticks([])
    i += obraz.shape[0] // len(osie.flatten())
plt.show()






