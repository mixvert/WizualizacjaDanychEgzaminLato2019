import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("dosw11.csv", sep=";")

plt.subplot(2, 1, 1)
plt.title("Wykres z wartością skrajną")
plt.plot(dane["Czas"], dane["Zmienna"], label="Zmienna")
plt.legend()

plt.subplot(2, 1, 2)
plt.title("Wykres bez wartości skrajnej")
out = dane[dane["Zmienna"] > 10]
dane["Zmienna"] = dane["Zmienna"].replace(200, 1.13)
plt.plot(dane["Czas"], dane["Zmienna"], label="Zmienna")
plt.legend()
plt.show()
