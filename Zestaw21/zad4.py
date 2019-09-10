import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dane = pd.read_csv("zlobki.csv", index_col=0)
zlobki = dane["Liczba dzieci"]
x = np.arange(4)

plt.bar(x, zlobki, color=["blue", "orange", "green", "brown"])
plt.title("Liczba dzieci w żłobkach na terenie Olsztyna")
plt.xticks(x, dane.index)
plt.savefig("wykres4.pdf")
plt.show()
