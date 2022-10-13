"""
@author: Aleksandra Zylka
"""

a = 3
b = 4
c = 5

boki = [a, b, c]

if not (a > 0 and b > 0 and c > 0):
    print('Wszystkie podane dlugości musza byc wieksze od zera')
else:
    if not (max(boki) < (sum(boki) - max(boki))):  #not a < (b + c) or b < (a + c) or c < (b + a)  
        print('trojkat nie powstanie - najdluzszy bok powinien '
        + 'byc mniejszy od sumy pozostalych bokow')
    else:
        o_pol = (a + b + c) / 2
        iloczyn = o_pol
        for i in range(len(boki) - 1):
            iloczyn *= o_pol - boki[i]
            pole = iloczyn**0.5
        print('Pole wynosi: ' + str(pole))
        
