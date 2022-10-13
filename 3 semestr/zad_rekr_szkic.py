
from re import I
import numpy as np
import itertools

obecne = [3, 1, 2]

def wszystkie_permutacje(ustawienie):
    for i in range(1, 10):
        permutacje = list(itertools.permutations(ustawienie))
    
    return permutacje

p = wszystkie_permutacje(obecne)

def lift_list(input_list):
    """
    List of nested lists becomes a list with the element exposed in the main list.
    :param input_list: a list of lists.
    :return: eliminates the first nesting levels of lists.
    E.G.
    >> lift_list([1, 2, [1,2,3], [1,2], [4,5, 6], [3,4]])
    [1, 2, 1, 2, 3, 1, 2, 4, 5, 6, 3, 4]
    """
    if input_list == []:
        return []
    else:
        return lift_list(input_list[0]) + (lift_list(input_list[1:]) if len(input_list) > 1 else []) \
            if type(input_list) is list else [input_list]

lista_cykli = lift_list(p)
#print(lista_cykli)

"""     TEGO NIE UŻYWASZ - ROBI LISTĘ W LIŚCIE
            BEZ SENSU
def cycles(perm):
  remain = set(perm)
  result = []
  while len(remain) > 0:
    n = remain.pop()
    cycle = [n]
    while True:
      n = perm.append(cycle)
      if n not in remain:
        break
      remain.remove(n)
      cycle.append(n)
    result.append(cycle)
  return result


cykle = cycles(lista_cykli)
"""


#rozkład permutacji na cykle proste
def is_valid_permutation(in_perm):
    """
    A permutation is a list of 2 lists of same size:
    a = [[1,2,3], [2,3,1]]
    means permute 1 with 2, 2 with 3, 3 with 1.
    :param in_perm: input permutation.
    """
    if not len(in_perm) == 2:
        return False
    if not len(in_perm[0]) == len(in_perm[1]):
        return False
    if not all(isinstance(n, int) for n in in_perm[0]):
        return False
    if not all(isinstance(n, int) for n in in_perm[1]):
        return False
    if not set(in_perm[0]) == set(in_perm[1]):
        return False
    return True

print(is_valid_permutation(lista_cykli))

c = 0

for i in range(1, 10):
    if not lista_cykli[i]:
        c += 1
        x = i
        while not lista_cykli(x):
            lista_cykli = True

