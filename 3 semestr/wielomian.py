"""
https://stackoverflow.com/questions/11856206/multivariate-polynomial-best-fit-curve-in-python 
"""

import numpy
import matplotlib.pyplot as plt
import multipolyfit as mpf

data = [[1,1],[4,3],[8,3],[11,4],[10,7],[15,11],[16,12]]
x, y = zip(*data)
plt.plot(x, y, 'kx')

stacked_x = numpy.array([x,x+1,x-1])
coeffs = mpf(stacked_x, y, 3) 
x2 = numpy.arange(min(x)-1, max(x)+1, .01) #use more points for a smoother plot
y2 = numpy.polyval(coeffs, x2) #Evaluates the polynomial for each x2 value
plt.plot(x2, y2, label="deg=3")
plt.show()