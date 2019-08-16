import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_csv("dosw17.csv", sep=";")

plt.subplot(2,1,1)
plt.title("Wykres z wartością skrajną")
plt.plot(dane["Czas"],dane["Zmienna"], label="Zmienna")
plt.legend()

plt.subplot(2,1,2)
plt.title("Wykres bez wartości skrajnej")
out=dane[dane["Zmienna"]>10]
dane["Zmienna"] = dane["Zmienna"].replace(200,np.nan)
plt.plot(dane["Czas"],dane["Zmienna"],label="Zmienna")
plt.legend()

plt.show()