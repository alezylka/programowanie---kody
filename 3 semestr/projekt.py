#Back-end
from tkinter import *


def parse_fasta_file(input_file):
    """Zwraca słownik {id:gene_seq} par na podstawie sekwencji
    znajdujących się we wprowadzanym pliku FASTA
    Args:
        input_file(FASTA): wprowadzany do funkcji plik
                            do stworzenia słownika
    Returns:
        parsed_seqs: sparsowane sekwencje białek
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

    #sklejenie całej sekwencji w słownik
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



# Graficzny interfejs

import PySimpleGUI as sg

uklad_1 = [  [sg.Text("Proszę o wybranie operacji")],
            [sg.Button("ZNAJDŹ DNA")],
            [sg.Button("ZNAJDŹ RNA")],
            [sg.Button("POKAŻ SEKWENCJĘ BIAŁKA")],
            [sg.Button("ZAKOŃCZ")]
            ]

window_1 = sg.Window('Menu', uklad_1)

while True:
    event, values = window_1.read()
    
    if event == sg.WINDOW_CLOSED or event == "ZAKOŃCZ":
        break
    elif event == 'ZNAJDŹ DNA':
        window_1.Hide()
        uklad_2 = [ [sg.Text('Wprowadź dane')],
                    [sg.InputText(key="nazwa_pliku"),
                    sg.FileBrowse('Wyszukaj plik...', target='nazwa_pliku'),
                    sg.Button('Otwórz', key='otworz')], 
                    [sg.Button("Anuluj")]
                    ]
        window_2 = sg.Window('Szukanie DNA', uklad_2, finalize=True)
        while True:
            event, values = window_2.read()
            if event == sg.WINDOW_CLOSED or event == "Anuluj":
                break
            elif event == "otworz":
                window_2.Hide()
                
                try:                                     
                    input_file = values['nazwa_pliku']               
                    f = open(input_file)                    
                    parsed_seqs = parse_fasta_file(input_file)

                    #wyodrębnienie członów ze słownika
                    for value in parsed_seqs:
                        lancuch = "value: %s" % (parsed_seqs[value])
                    
                    #zamiana typu słownik na tekst
                    bialka_1 = str(lancuch)
                    #rozpoczęcie odczytu tekstu od początku kodu białek
                    bialka_2 = bialka_1.split(": ", 1)[1]
                    
                    DNA_here = string_do_DNA(bialka_2)

                    uklad_2_2 = [ [sg.Text("Otrzymany łańcuch DNA to ")], [sg.popup(DNA_here)] ]
                    window_2_2 = sg.Window(uklad_2_2)
                except:
                    sg.popup("Wprowadzonych danych nie można przetworzyć")  

                window_2.close()
                window_1.UnHide()

    elif event == 'ZNAJDŹ RNA':
        window_1.Hide()
        uklad_3 = [ [sg.Text('Wprowadź dane')],
                    [sg.InputText(key="nazwa_pliku"),
                    sg.FileBrowse('Wyszukaj plik...', target='nazwa_pliku'),
                    sg.Button('Otwórz', key='otworz')], 
                    [sg.Button("Anuluj")]
                    ]
        window_3 = sg.Window("Szukanie RNA", uklad_3, finalize=True)
        while True:
            event, values = window_3.read()
            if event == sg.WINDOW_CLOSED or event == "Anuluj":
                break
            elif event == "otworz":
                window_3.Hide()
                try:
                    input_file = values['nazwa_pliku']               
                    f = open(input_file)                    
                    parsed_seqs = parse_fasta_file(input_file)

                    #wyodrębnienie członów ze słownika
                    for value in parsed_seqs:
                        lancuch = "value: %s" % (parsed_seqs[value])
                
                    #zamiana typu słownik na tekst
                    bialka_1 = str(lancuch)
                    #rozpoczęcie odczytu tekstu od początku kodu białek
                    bialka_2 = bialka_1.split(": ", 1)[1]
                
                    RNA_here = bialka_do_RNA(bialka_2)

                    uklad_3_3 = [ [sg.Text("Otrzymany łańcuch RNA to ")],
                                    [sg.popup(RNA_here)] ]
                    window_3_3 = sg.Window(uklad_3_3)
                except:
                    sg.popup("Wprowadzonych danych nie można przetworzyć")

                window_3.close()
                window_1.UnHide()

    elif event == 'POKAŻ SEKWENCJĘ BIAŁKA':
        window_1.Hide()
        uklad_4 = [ [sg.Text('Wprowadź dane')],
                    [sg.InputText(key="nazwa_pliku"),
                    sg.FileBrowse('Wyszukaj plik...', target='nazwa_pliku'),
                    sg.Button('Otwórz', key='otworz')], 
                    [sg.Button("Anuluj")]
                    ]
        window_4 = sg.Window("Szukanie sekwencji białka", uklad_4, finalize=True)
        while True:
            event, values = window_4.read()
            if event == sg.WINDOW_CLOSED or event == "Anuluj":
                break    
            elif event == "otworz":
                window_4.Hide()

                try:                  
                    input_file = values['nazwa_pliku']               
                    f = open(input_file)                    
                    parsed_seqs = parse_fasta_file(input_file)

                    #wyodrębnienie członów ze słownika
                    for value in parsed_seqs:
                        lancuch = "value: %s" % (parsed_seqs[value])
                    
                    #zamiana typu słownik na tekst
                    bialka_1 = str(lancuch)
                    #rozpoczęcie odczytu tekstu od początku kodu białek
                    bialka_2 = bialka_1.split(": ", 1)[1]

                    uklad_4_4 = [ [sg.Text("Sekwencja białek z wprowadzonego pliku: ")],
                                    [sg.popup(bialka_2)] ]
                    window_4_4 = sg.Window(uklad_4_4)
                except:
                    sg.popup("Wprowadzonych danych nie można przetworzyć")
            
                window_4.close()
                window_1.UnHide()
       
## Jestem świadoma, że powtarzający się kod jest niezgody ze sztuką programowania 
## niestety napotkałam za dużo niepowodzeń w wywoływaniu kilku funkcji na raz

