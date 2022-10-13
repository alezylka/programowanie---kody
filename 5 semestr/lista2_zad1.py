
import math

#x = (math.sqrt(2)**2-2)

#print(x)

y = 4.0 #what are the concequences
        #of 
#Em - machine precision - gap between
# smallest number (greater than 1) and typed one

#print(type(y))

small = 1/2**49
#print(small)

for i in range(5):
    small /= 2
    #print(i, 1 + small, small)

#print(1/2**52)

xt = 0.1
yt = 0.2
zt = 0.3

#print(zt == xt+yt)

#print(zt - (xt + yt))

#print((abs(zt-(xt+yt)) < 1.0e-12))

#wart funkcji wykladniczej = wartosc
# sumy nieskonczonego szeregu

#zadanie 1 z listy
def silnia(z_liczby):
    if z_liczby > 1:
        return z_liczby*silnia(z_liczby-1)
    return 1

def szereg(nmax):
    sumowanie = []
    n = 0
    for x in range(0, nmax):
        n += ((x**i)/(silnia(i)))
        sumowanie.append(n)
    return(sumowanie)

print(szereg(5))

print(math.exp(5))
