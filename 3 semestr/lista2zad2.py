"""""
@author: Aleksandra Zylka
"""""


(x, y) = (5, 0)
try:
    z = x/y
except ZeroDivisionError as e:
    z = e

print(z)

while True:
    try:
        x = float(input("Wprowadz liczbe..."))
        break
    except ValueError:
        print("zamien na kropke i sprobuj ponownie")

