import matplotlib.pyplot as plt
import pandas as pd

# ładujemy dane jako ramkę, sep ustawiania inny niż domyślny separator,
# header na None - nie ustawia pierwszego wiersza jako nagłówka
dane = pd.read_csv("sport.csv", sep=";", header=None)
# pomocnicza krotka aby wysunąć największą część
explode = (0.1, 0, 0, 0, 0, 0)
# tytuł
plt.title("Wykres popularności sportów")
# tekst z numerem indeksu, pierwsze dwa argumenty określają współrzędne
plt.text(-1, 1, "12345")
# wykres kołowy, pierwszy argument to dane do generowania wykresu
# labels - etykiety do wykresu, autpct - formatowanie procentów
# explode - wysunięcie wycinków koła
plt.pie(dane.iloc[:, 1], labels=dane.iloc[:, 0], autopct='%1.f%%', explode=explode)
# zapis do pliku w formacie pdf
plt.savefig("wykres4.pdf")
# pokazanie wykresu
plt.show()