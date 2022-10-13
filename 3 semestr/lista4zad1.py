
import numpy as np
import matplotlib.pyplot as plt

#n = np.logspace(0, 20, int(2e4), dtype=np.float16)
#n = np.logspace(0, 20, int(2e4), dtype=np.float32)
n = np.logspace(0, 20, int(2e4), dtype=np.float64)
e = (1 + 1 / n) ** n


for i in range(len(e)-1):
    if (e[i] > e[i + 1]):
        punkt_n = n[i]
        punkt_e = e[i]
        break


print([punkt_n, punkt_e])


#liczenie pochodnych e i n i zwracanie krotek
e_poch = np.diff(e) 
n_poch = np.where(e_poch < 0)
n_poch = n_poch[0][0]
punkt_e_1 = e[n_poch]
punkt_n_1 = n[n_poch]
print([punkt_n_1, punkt_e_1])

#rysowanie
plt.semilogx(n, e, "b", label="$e(n) = (1 + 1/n)^n$")
plt.semilogx(punkt_n_1, punkt_e_1, "rx",
                label="Punkt zachwiania monotonicznosci")
plt.legend(loc="upper left")
plt.xlim(left=1)
plt.xlim(right=1e20)
plt.show()
