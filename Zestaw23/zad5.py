import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dane = pd.read_csv("sklepy.csv")
rodzaj = dane["Rodzaj sklepu"]
liczba = dane["Liczba"]
x = np.arange(4)

plt.barh(x, liczba, color="orange")
plt.yticks(x, rodzaj)
plt.grid()
plt.xticks([0, 100, 200, 300])
plt.title("Rodzaje sklepów na terenie woj. warm.-maz. w 2017 roku")
plt.show()
