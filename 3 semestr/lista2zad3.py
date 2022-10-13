"""
@author: Aleksandra Zylka
@sources: Wyklad 2
"""

def transkrybuj(dna):
    """
    Transkrypcja DNA na RNA.
    Args:
        dna (str): sekwencja DNA składająca się z~liter ACGT
    Returns:
        rna: sekwencja RNA składająca się z~liter ACGU
    Raises:
        TypeError: jeśli sekwencja DNA nie jest ciągiem znaków
        ValueError: jeśli sekwencja DNA zawiera litery inne niż ACGT
    """
    if not isinstance(dna, str):
        raise TypeError('Podana sekwencja DNA '
                        'nie jest ciągiem znaków!')
    rna = ''
    for z in dna:
        if z in ['A','C','G']:
            rna += z
        elif z == 'T':
            rna += 'U'
        else:
            raise ValueError('Podana sekwencja DNA zawiera '
                                'inne litery niż ACGT!')
    return rna

#transkrybuj('AUUGTACAAA')

def wyjatek(kod):
    """
    Wykorzytsanie mechanizmu wyjątków.
    Sprawdzenie, czy dane wejściowe ograniczają się do A, T, C, G.
    Args:
        kod(str): sekwencja DNA sprawdzana przez program
    Returns:
        nowy kod(str): sekwencja RNA transkrybowana przez funkcje transkrybuj(DNA)
    Raises:
        ValueError: jeśli sekwencja DNA zawiera litery inne niż ACGT
    """

    nowy_kod = ''

    for x in kod:
        try:
            nowy_kod = transkrybuj(kod)
        except ValueError:
            nowy_kod = None
    return nowy_kod

print(wyjatek('ACGTGTTTAA'))