
import numpy as np
import matplotlib.pyplot as plt


#n = np.logspace(0, 20, int(2e4), dtype=np.float16)
#n = np.logspace(0, 20, int(2e4), dtype=np.float32)
n = np.logspace(0, 20, int(2e4), dtype=np.float64)
# ...
e = (1 + 1 / n) ** n

#first = True
for i in range(len(e)-1):
    if (e[i+1] < e[i]):
        n_c1 = n[i]
        e_c1 = e[i]
        break  # instead of the flag 'first'
        #first = False


print([n_c1, e_c1])

# the second version with differentiating (liczenie pochodnej)
e_diff = np.diff(e) # count differences between elements == differentiate, notice: len(e_diff) = len(e) - 1
n_diff = np.where(e_diff < 0) # returns tuple, now we want to extract ndarray with indices, and then take the first index
n_diff = n_diff[0][0]  # ndarray extracted n_diff[0], the first index taken [0]
n_c2 = n[n_diff]  # the first 'zero' location found
e_c2 = e[n_diff]
print([n_c2, e_c2])

plt.semilogx(n, e, "b", label="$e(n) = (1 + 1/n)^n$")
plt.semilogx(n_c1, e_c1,"rx", label="Monotonicity-violation point")
plt.legend(loc="upper left")
plt.xlim(left=1)
plt.xlim(right=1e20)
plt.show()
