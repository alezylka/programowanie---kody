"""
@author: Aleksandra Zylka
@sources: https://docs.python.org/3/library/exceptions.html 
        https://docs.python.org/3/library/types.html 
"""

#1 TypeError błąd typu danych - string zamiast integer'a

print('Odliczam:')
for i in range('d'):
    print(i)


#2 DivisionError błąd dzielenia przez 0
"""
try:
   print(1/0)
except:
   print("Coś poszło nie tak")
"""

#3 NameError błąd nazwy, niezdefiniowany x
"""
try:
  print(x)
except:
  print("Wystąpił błąd")
"""


#4 ModuleNotFoundError błąd modułu - wywołanie nieistniejącej biblioteki
"""
from types import ModuleType
import Biblioteka_X

if Biblioteka_X is not ModuleType:
  raise ModuleNotFoundError
"""
