from backend import DataGrabber
from pathlib import Path
import matplotlib.pyplot as plt

def get_response(message, options):
    print(message)
    for i, opt in enumerate(options):
        print(f"{i+1}. {opt}")
    
    while True:
        try:
            response = int(input(">> "))
            if response in range(1, len(options)+1):
                return response - 1
            else:
                print("Niepoprawna liczba.")
        except ValueError:
            print("Niepoprawnie podane dane.")

def get_row_data():
    row_data = {}
    print("Wprowadz dane nowego wiersza.")
    row_data["typ"] = input("Typ: ")
    while True:
        try:
            row_data["cena"] = float(input("Cena: "))
            break
        except ValueError:
            print("Niepoprawnie podana cena. Podaj ponownie.")
    return row_data

if __name__ == "__main__":
    backend = DataGrabber(Path("studia/programowanie - kody/projekt/data.csv"))
    while True:
        options = ["Dodaj", "Wykres", "Wyświetl", "Zapisz", "Wyjście"]
        message = "Witaj w menu!\n Wybierz opcję:"
        resp = get_response(message, options)
        if resp == 0:
            row_data = get_row_data()
            backend.append_row(row_data)
        elif resp == 1:
            fig = backend.plot_data()
            fig.show()
        elif resp == 2:
            print(backend.get_groups())
        elif resp == 3:
            backend.save_data()
        else:
            print("Wyłączyłeś program.")
            break

