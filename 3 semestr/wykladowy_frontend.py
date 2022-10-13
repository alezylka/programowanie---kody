
import PySimpleGUI as sg
import csv
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('Agg')

def wczytaj_serie(nazwa_pliku):
    with open(nazwa_pliku) as plik:
        czytnik = csv.reader(plik)
        naglowek = next(czytnik)
    return [seria.replace(' ',' ').strip() for seria in naglowek]

def wczytaj_dane(nazwa_pliku, seria):
    dane = []
    with open(nazwa_pliku) as plik:
        czytnik = csv.reader(plik)
        next(czytnik)
        for wiersz in czytnik:
            try:
                dane.append(float(wiersz[seria]))
            except:
                print("Pominięto rekord: " + str(wiersz))
    return dane

def utworz_wykres(osie, dane, nazwa_serii, linia=False):
    osie.clear()
    if linia:
        osie.plot(dane,'-')
    else:
        osie.plot(dane,'.')
    osie.set_ylabel(nazwa_serii)
    osie.set_xlabel("pozycja")


#klawisz zamknij
#lista list z kolejnymi elementami okna
uklad = [   [sg.Text('Plik z danymi w formacie csv:')],
            [sg.InputText(key='nazwa_pliku'),
             sg.FileBrowse('Wybierz...', target='nazwa_pliku'),
             sg.Button('Otwórz', key='otworz')],
            [sg.Text('Seria:'),
             sg.Listbox([], key='nazwa_serii', enable_events=True),
             sg.Checkbox('Łącz punkty', key='linia'),
             sg.Button('Rysuj', visible=False)],
            [sg.Canvas(key='plotno')],
            [sg.InputText(key='nazwa_pliku_wykresu'),
             sg.FileBrowse('Wybierz...', target='nazwa_pliku_wykresu'),
             sg.Button('Zapisz', visible=False)],
            [sg.Button('Zamknij')]
        ]

#zmienna okna programu
okno = sg.Window('Wizualizacja serii danych', uklad)


rysunek = plt.figure()
plotno_rysunku = FigureCanvasTkAgg(rysunek, okno['plotno'].TKCanvas)
plotno_rysunku.get_tk_widget().pack()


#zamykanie okna programu
while True:
    zdarzenie, wartosci = okno.read()
    
    #po naciśnięciu klawisza Otworz
    if zdarzenie == 'otworz':
        try:
            moje_serie = wczytaj_serie(wartosci['nazwa_pliku'])
            okno['nazwa_serii'].update(moje_serie)
            okno['Rysuj'].update(visible=False)
        except:
            sg.Popup('Nie udało się otworzyć pliku!', title='Błąd')
            okno['nazwa_serii'].update([])
    
    #obsługa zdarzenia wyboru z listy
    if zdarzenie == 'nazwa_serii':
        okno['Rysuj'].update(visible=True)

    if zdarzenie == 'Rysuj':
        try:
            dane = wczytaj_dane(wartosci['nazwa_pliku'],
                    moje_serie.index(wartosci['nazwa_serii'][0]))
            utworz_wykres(rysunek.gca(), dane, wartosci['nazwa_serii'][0],
                    linia = wartosci['linia'])
            plotno_rysunku.draw()
            okno['Zapisz'].update(visible=True)
        except:
            sg.Popup('Nie udało się utwrzyć wykresu, sprawdź swoje dane!',
                    title='Błąd')

    if zdarzenie == 'Zapisz':
        try:
            plt.savefig(wartosci['nazwa_pliku_wykresu'])
        except:
            sg.Poput('Nie udało się zapisać wykresu!', title='Błąd')

    if zdarzenie == sg.WIN_CLOSED or zdarzenie == 'Zamknij':
       break 
        
plt.close(rysunek)
okno.close()


