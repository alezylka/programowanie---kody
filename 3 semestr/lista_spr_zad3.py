import pandas as pd

def konwersja(st_cel):
    """Konwersja jednostek temperatury ze stopni
        Celsjusza na Kelviny
    
    Args:
    st_cel(float): stopnie celsjusza wprowadzanie do funkcji

    Returns:
    kelwiny(float): wartość Kelvinów zwracana przez funkcję
    """
    kelwiny = st_cel + 273.15
    
    return kelwiny

celsjusz = float(input('Wprowadz temperaturę w Celsjuszach... '))

zamieniona = konwersja(celsjusz)

print("Zamieniona temperatura " + str(celsjusz) +\
        " st. Celsjusza ma teraz wartość " + str(zamieniona) + " Kelwinów.")

dframe = {'celsjusz': [celsjusz], 'kelwin': [zamieniona]}

ramka = pd.DataFrame(dframe)
ramka.to_csv('konwersja.csv')
