import argparse
from backend import DataGrabber
from pathlib import Path
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Program pokazowy')
parser.add_argument('-a', "--add", action="store", dest="add", nargs=2, help="Dodaje nowy wiersz do pliku o typie argumentu 1 i cenie argumentu 2")
parser.add_argument('-s', "--show", action="store_true",  help="Wyświetla pogrupowany plik")
parser.add_argument('-p', "--plot", action="store_true",  help="Wyświetla wykres")


args = parser.parse_args()
grabber = DataGrabber(Path("studia/programowanie - kody/projekt/data.csv"))


if args.add:
    try:
        grabber.append_row({"typ": args.add[0], "cena": float(args.add[1])})
    except:
        print("Niepoprawne dane")
    grabber.save_data()
if args.show:
    print(grabber.get_groups())
if args.plot:
    fig = grabber.plot_data()
    plt.show()


