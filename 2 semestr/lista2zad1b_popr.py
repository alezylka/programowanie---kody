"""
@author: Aleksandra Zylka
"""

#definiowanie zmiennych
Ap = -3
Ak = 7
Bp = 4
Bk = 8

krance_odc = [Ap, Ak, Bp, Bk]

#zalozenie Ap > Ak oraz Bp > Bk

if not (Ap < Ak and Bp < Bk):
   print('niespelniony warunek Ap < Ak lub B < Bk')
else:
    if Bp >= Ap and Bp <= Ak:
        if Bk <= Ak:
            cz_wspolna = Bk - Bp        #odcinek A zawiera się w odcinku B lub na odwrot
        else:
            cz_wspolna = Ak - Bp        #odcinki nachodza na siebie lub stykaja sie
    else:
        if not(Bk < Ap and Bk > Ak):
          cz_wspolna = Bk - Ap          #odcinki nachodza na siebie lub sie stykaja       
        elif Bp <= Ap and Bk > Ak:
            cz_wspolna = Ak - Ap        #odcinek A zawiera się w odcinku B
        else:
            cz_wspolna = 0              #brak czesci wspolnej

print('Dlugosc czesci wspolnej wynosi: ' + str(cz_wspolna))