import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dane = pd.read_csv("waluta.csv")
dzien=dane["Dzień"]
kurs=dane["Kurs CAD"]

plt.plot(dzien, kurs, color="orange")
plt.plot([0,30],[2.95,2.95], color="green", linestyle="dashed")
plt.ylim([2.9,3])
plt.title("Kurs dolara kanadyjskiego w sierpniu 2019")
plt.xlabel("Sierpień 2019")
plt.show()