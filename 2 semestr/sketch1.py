"""
@author: Aleksandra Zylka
"""

a = 3
b = 4
c = 5

#o_pol := (a + b + c) / 2

iloczyn := o_pol * (o_pol - a) * (o_pol - b) * (o_pol - c)
pole := iloczyn ** 0.5

print('a + b + c :' + str(o_pol))
print('Pole wynosi' + str(pole))