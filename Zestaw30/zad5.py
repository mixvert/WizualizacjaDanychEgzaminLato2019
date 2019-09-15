import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dane = pd.read_csv("sklepy.csv")
rok16 = dane[dane["Rok"] == 2016]
rok17 = dane[dane["Rok"] == 2017]
x = np.arange(3)

plt.bar(x, rok16["Liczba obiektów"], label="Rok 2016", width=0.33)
plt.bar(x + 0.33, rok17["Liczba obiektów"], label="Rok 2017", width=0.33)
plt.xticks(x + 0.165, rok16["Rodzaj sklepu"])
plt.title("Informacje o sklepach")
plt.legend()
plt.show()
