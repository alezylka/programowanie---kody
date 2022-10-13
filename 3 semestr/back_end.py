"""
@sources: https://colab.research.google.com/github/
            zaneveld/full_spectrum_bioinformatics/blob/master/content/
            06_biological_sequences/reading_and_writing_fasta_files.
            ipynb#scrollTo=eibNxBDnshjc ;
            
"""

#FUNKCJE

def parse_fasta_file(input_file):
    """Zwraca słownik {id:gene_seq} par na podstawie sekwencji
    znajdujących się we wprowadzanym pliku FASTA
    Args:
        input_file(FASTA): wprowadzany do funkcji plik
                            do stworzenia słownika
    """
    parsed_seqs = {}
    curr_seq_id = None
    curr_seq = []

    for line in f:
        line = line.strip()

        if line.startswith(">"):
            if curr_seq_id is not None:
                parsed_seqs[curr_seq_id] = ''.join(curr_seq)

            curr_seq_id = line[1:]
            curr_seq = []
            continue

        curr_seq.append(line)

    #Add the final sequence to the dict
    parsed_seqs[curr_seq_id] = ''.join(curr_seq)
    return parsed_seqs



def bialka_do_RNA(protein):
    """Funkcja przetwarzająca łańcuch białkowy na DNA.
    Args:
        protein(str): łańcuch jednoliterowych symboli białek.
    Returns:
        RNA(str): łańcuch przetworzonych danych wejściowych,
                    czyli sekwencja RNA
    Raises:
        ValueError: gdy łańcuch tekstu poddanego
                    operacji nie ma znaków
    """

    bialka_RNA = str.maketrans({ ord("A"): "GCUGCCGCAGCG",
                    ord("C"): "UGUUGC", ord("D"): "GAUGAC",
                    ord("E"): "GAAGAG", ord("F"): "UUUUUC",
                    ord("G"): "GGUGGCGGAGGG", ord("H"): "CAUCAC",
                    ord("I"): "AUUAUCAUA", ord("K"): "AAAAAG",
                    ord("L"): "CUUCUCCUACUG", ord("M"): "AUG",
                    ord("N"): "AAUAAC", ord("P"): "CCUCCCCCACCG",
                    ord("Q"): "CAACAG", ord("R"): "CGUCGCCGACGG",
                    ord("S"): "UCUUCCUCAUCG",
                    ord("T"): "ACUACCACAACG",
                    ord("V"): "GUUGUCGUAGUG", ord("W"): "UGG", 
                    ord("Y"): "UAUUAC"
                })

    if len(protein) != 0:
        RNA = protein.translate(bialka_RNA)
    else:
        raise ValueError("Zmienna poddana operacji\
                            nie ma żadnych znaków")

    return RNA


def string_do_DNA(biodata):
    """Funkcja poddająca wprowadzony ciąg znaków (RNA)
        odwróconej stranskrypcji.
    Args:
        biodata(str): dane łańcucha RNA
    Returns:
        DNA(str): sekwencja DNA
    """

    tekst_DNA = str.maketrans({ ord("U"): "T" })


    if len(biodata) != 0:
        #rozgałęzienie na dwa sposoby otrzymania RNA
        # w zależności od rodzaju danych wejściowych DNA/białko
        if 'U' not in biodata:
            DNA_1 = bialka_do_RNA(biodata)
            DNA = DNA_1.translate(tekst_DNA)
        else:
            DNA = biodata.translate(tekst_DNA)
    else:
        raise ValueError("Zmienna poddana operacji\
                            nie ma żadnych znaków")

    return DNA





#zagnieżdżenie pliku FASTA w zmiennej
input_file = 'sequence.fasta'

f = open(input_file)
parsed_seqs = parse_fasta_file(input_file)

#wyodrębnienie członów ze słownika
for value in parsed_seqs:
    lancuch = "value: %s" % (parsed_seqs[value])
#    print(lancuch)

#zamiana typu słownik na tekst
bialka_1 = str(lancuch)

#rozpoczęcie odczytu tekstu od początku kodu białek
bialka_2 = bialka_1.split(": ", 1)[1]


#TESTY WYNIKÓW POSZCZEGÓLNYCH OPERACJI
# NA ŁAŃCUCHACH TEKSTÓW

#print(bialka_2)

#print(bialka_do_RNA(bialka_2))
#print(string_do_DNA("GAAUCAUA"))
#print(string_do_DNA(bialka_2))
