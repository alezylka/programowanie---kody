"""
@author: Aleksandra Żyłka
@sources: https://www.biostars.org/p/461697/
            https://stackoverflow.com/questions/14360389/getting-file-path-from-command-line-argument-in-python
            https://biopython.org/docs/1.75/api/Bio.SeqIO.html
"""

#1. argument - ścieżka pliku, otworzyć plik
#2. pandas, zapisać do tabeli - 3 kolumny: nazwa organizmu, nazwa białka, sekwencja
#3. znaleźć duplikaty sekwencji - funkcja z biblioteki pandas
#4. DataFrame z sekwencjami zapisać w .csv i .json
#5. komentarze, obsłga błędów

#import bibliotek
import os
import pandas
from Bio import SeqIO

#ścieżka pliku jako argument
sciezka = "\Komputer\(F:)\studia"
folder = "python"
plik = "uniprot.fasta"
argument = os.path.join(sciezka, folder, plik)

print(argument)

#otwarcie pliku
with open('uniprot.fasta') as fasta_file: 
    nazwa_białka = []
    długość = []
    for seq_record in SeqIO.parse(fasta_file, 'fasta'):
        nazwa_białka.append(seq_record.id)
        długość.append(len(seq_record.seq))

#tworzenie tabeli
dataframe = pandas.DataFrame(dict(ID=nazwa_białka, length=długość)).set_index(['ID'])

#drukowanie dataframe'u
print(dataframe)

#zapis w .csv:
#dataframe.to_csv('uniprot_1.csv')

