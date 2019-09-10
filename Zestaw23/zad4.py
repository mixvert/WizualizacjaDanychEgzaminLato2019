import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("dosw23.csv")
czas = dane["Czas"]
zm1 = dane["Zmienna1"]
zm2 = dane["Zmienna2"]
plt.plot(czas, zm1, "b.", label="Zmienna 1")
plt.plot(czas, zm2, "g--", label="Zmienna 2")
plt.title("Wyniki doświadczenia")
plt.legend()
plt.savefig("wykres4.pdf")
plt.show()
