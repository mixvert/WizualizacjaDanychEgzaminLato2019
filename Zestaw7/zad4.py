import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("dosw7.csv", sep=";")

plt.plot(dane["Czas"], dane["Zmienna1"], linestyle="dashed", color="blue", label="Zmienna1")
plt.plot(dane["Czas"], dane["Zmienna2"], linestyle="solid", color="green", label="Zmienna2")
plt.legend(loc="lower left")
plt.ylabel("Zmienne")
plt.xlabel("Czas")
plt.grid()
plt.title("Wyniki doświadczenia")
plt.savefig("Wykres4.png")
plt.show()
