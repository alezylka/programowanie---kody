import PySimpleGUI as sg
from backend import DataGrabber
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

layout = [[sg.Text("Witaj w programie! Wybierz opcję", key='-TEXT-')],
          [sg.Button('Dodaj rekord')],
          [sg.Button('Pokaz wykres')],
          [sg.Button('Wyswietl')],
          [sg.Button('Zapisz zmiany')],
          [sg.Button('Wyjdz')]
          ]
          
window = sg.Window('Menu', layout)
grabber = DataGrabber(Path("studia\programowanie - kody\projekt\data.csv"))

while True:
    event, values = window.read() 
    if event == sg.WINDOW_CLOSED or event == 'Wyjdz':
        break
    elif event == 'Dodaj rekord':
        window.Hide()
        op_lst = ["rzecz", "bilet", "inne"]
        new_window = sg.Window('Podaj dane', 
                    layout=[[sg.Text('Podaj typ'),
                    sg.Combo(op_lst, readonly= True)],
                    [sg.Text('Podaj cene'), sg.InputText()],
                    [sg.Button('Dodaj'), sg.Button('Anuluj')]])
        while True:
            event, values = new_window.read()
            if event == sg.WINDOW_CLOSED or event == 'Anuluj':
                break
            elif event == 'Dodaj':
                try:
                    grabber.append_row({"typ": values[0], "cena": float(values[1])})
                except:
                    sg.Popup("Niepoprawne dane")
                break
        new_window.close()
        window.UnHide()
    elif event == 'Pokaz wykres':
        window.Hide()
        new_window = sg.Window('Wykres', layout=[[sg.Canvas(key='-CANVAS-')],
        [sg.Button('Zamknij')]], finalize=True)
        draw_figure(new_window['-CANVAS-'].TKCanvas, grabber.plot_data(pyplot=False))
        while True:
            event, values = new_window.read()
            if event == sg.WINDOW_CLOSED or event == 'Zamknij':
                break
        new_window.close()
        window.UnHide()
    elif event == 'Wyswietl':
        sg.popup(grabber.get_groups())
    elif event == 'Zapisz zmiany':
        grabber.save_data()
        window["-TEXT-"].update("Zapisano zmiany.")

window.close()