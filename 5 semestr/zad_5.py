#7.5

def sumuj(liczba):
    a = 0
    if liczba > 0:
        if liczba % 2 != 0:
            for i in range (1, liczba):
                a += i
            out = a
        else:
            out = "Wprowadz liczbe nieparzysta."
    else:
        out = "Wprowadz liczbe wieksza od zera."
    return out

print(sumuj(5))