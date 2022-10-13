"""
@author: Zylka Aleksandra
"""

from struktury_dynamiczne import stos, lista2


#uzycie listy

moja_lista = lista2.utworz_liste()
lista2.dopisz(moja_lista, "56")
lista2.dopisz(moja_lista, "pies")
lista2.dopisz(moja_lista, "mrowka")
test = lista2.zwroc(moja_lista, 2)
print('Zwrocony element to ' + str(test))


#uzycie stosu

moj_stos = stos.utworz_stos()
stos.na_stos(moj_stos, "(<")
stos.na_stos(moj_stos, ":?")
proba = stos.ze_stosu(moj_stos)
proba += stos.ze_stosu(moj_stos)
assert proba == ':?(<', 'Niepoprawnie ulozony stos'
print('Poprawnie ulozony stos daje napis: ' + str(proba))
