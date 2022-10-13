def sekwencja_RNA(DNA):
    """Funkcja przyporządkowuje sekwencje RNA dla nici matrycowej DNA.
    Args:
        DNA (str): nic kodujaca DNA
    Returns:
        rev_DNA.replace...(str): znaleziona sekwencja nici RNA
        None: w przeciwnym wypadku, brak danych do zwrocenia
    """
    
    if not(len(DNA) == 0):
        if any(x not in allowed_characters for x in DNA):
            return None
        else:
            rev_DNA = DNA[::-1]   #odczytanie tablicy DNA od tylu
            return(rev_DNA.replace('A','u').replace('T','a').replace('C','g').replace('G','c').upper()) #operacja transkrypcji DNA               
    else: #jesli string jest pusty
        return None

allowed_characters = ['A', 'C', 'G', 'T']
DNA = "ATCGTPGGA"
sekwencja_RNA(DNA)
print(sekwencja_RNA(DNA))
