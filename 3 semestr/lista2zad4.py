"""
@author: Zylka Aleksandra
"""

from struktury_dynamiczne import stos, lista2
#, królik
#, więcej_stosów

#użycie listy

moja_lista = lista2.utworz_liste()

lista2.dopisz(moja_lista, "56")
lista2.dopisz(moja_lista, "pies")
lista2.dopisz(moja_lista, "mrowka")

test = lista2.zwroc(moja_lista, 1)
#print('Zwrocony element to ' + str(test))

#Zgłaszanie wyjątków

#AssertionError - wywołano indeks, którego nie ma w liście

try:
    print(lista2.zwroc(moja_lista, 8))
except:
    print(AssertionError)


#NameError - wywołano błędną nazwę listy
"""
#lista40 zamiast 'lista2'
try:
    lista40.dopisz(moja_lista, 'kwiatek')
    test_2 = lista2.zwroc(moja_lista, 3)
    print(test_2)
except:
    print(NameError)


def zepsuta_lista():
    i = twoja_lista
    if i is not moja_lista:
        raise NameError

print(zepsuta_lista)
"""
#AttributeError - wywołano nieistniejący atrybut z modułu 'struktury dynamiczne'
"""
#oddaj zamiast 'zwroc'
try:
    lista2.zapisz(moja_lista, 'pakiet')
    print(lista2.oddaj(moja_lista, 4))
except:
    print(AttributeError)

def teest():
    test_3 = lista2.oddaj(moja_lista, 2)
    if test_3 != 'mrowka':
        raise AttributeError

print(teest)
"""

#ImportError - wywołano nieistniejący program z modułu 'Stryktury dynamiczne'
"""
#krolik zamiast 'lista2'
try:
    królik.dopisz(moja_lista, 'szklanka')
    nowa_lista = lista2.zwroc(moja_lista, 0)
    print(nowa_lista)
except:
    print(ImportError)
"""

#użycie stosu

moj_stos = stos.utworz_stos()                                   #tworzenie stosu

stos.na_stos(moj_stos, "(<")                                    #układanie elementów na stosie
stos.na_stos(moj_stos, ":?")

proba = stos.ze_stosu(moj_stos)                                 #zdejmowanie elementów ze stosu
proba += stos.ze_stosu(moj_stos)

assert proba == ':?(<', 'Niepoprawnie ulozony stos'             #sprawdzenie poprawności działania kodu
print('Poprawnie ulozony stos daje napis: ' + str(proba))       #generacja rezultatu

#Zgłaszanie wyjątków

#TypeError - w poniższym przypadku chcę więcej zdjąć ze stosu, niż na niego nałożyłam

try:
    proba += stos.ze_stosu(moj_stos)
except:
    print(TypeError)


#AttributeError - wywołano nieistniejący atrybut z modułu 'struktury dynamiczne'

try:
    stos.przed_stos(moj_stos, "drzewo")
except:
    print(AttributeError)


#NameError - użycie niepoprawnej nazwy stosu
"""
try:
    otrzymanie = stos.ze_stosu(twoj_stos)
    print(otrzymanie)
except:
    print(NameError)


#ImportError - wywołano nieistniejący program z modułu 'Stryktury dynamiczne'

try:
    więcej_stosów.na_stos(moj_stos, 'koniczyna')
    zdejmowanie = stos.ze_stosu(moj_stos, 0)
    print(zdejmowanie)
except:
    print(ImportError)
"""