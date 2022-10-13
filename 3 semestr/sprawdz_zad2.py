import numpy as np

def kalkulator(dzialanie, wartosci):
    """Funkcja dzialajaca jak prosty kalkulator.
    Args:
        dzialanie (str): nazwa wymaganego dzialania
        wartosci (list): lista potrzebnych wartosci
    Rerutns:
        wynik (int): wynik dzialania

    """


    if dzialanie == 'dodawanie':
        suma = sum(wartosci)
        return ("suma wartosci z listy wynosi " + str(suma))

    if dzialanie == 'odejmowanie':
        for i in wartosci:
            x = wartosci[0]
            y = sum(wartosci[1 : (i-1)])
            roznica = np.subtract(x, y)
        return ("roznica wartosci z listy wynosi " + str(roznica))

    if dzialanie == 'mnozenie':
        mnozenie = np.prod(np.array(wartosci))
        return ("iloczyn wartosci z listy wynosi " + str(mnozenie))

    if dzialanie == 'dzielenie':
        if len(wartosci) == 2:
            x = wartosci[0]
            y = wartosci[1]
            dziel = x / y
            return ("dzielenie wartosci z listy wynosi " + str(dziel))

            

print(kalkulator('dzielenie', [12, 2, 1]))

def test_dodawanie():
    lista1 = [2, 5, 8, 3]
    dod = 'dodawanie'
    test1 = kalkulator(dod, lista1)
    assert (test1 == 18)

def test_odejmowanie():
    lista2 = [13, 9]
    odej = 'odejmowanie'
    test2 = kalkulator(odej, lista2)
    assert (test2 == 4)

def test_mnozenie():
    lista3 = [10, 10]
    mno = 'mnozenie'
    test3 = kalkulator(mno, lista3)
    assert (test3 == 100)

def test_dzielenie():
    lista4 = [12, 2]
    dzielenie = 'dzelenie'
    test4 = kalkulator(dzielenie, lista4)
    assert (test4 == 6)
