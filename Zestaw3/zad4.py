import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("dosw3.csv", sep=";")

plt.plot(dane["Czas"], dane["Zmienna"], linestyle="dashed", color="green", label="Zmienna")
plt.legend()
plt.ylabel("Zmienna")
plt.xlabel("Czas")
plt.title("Wyniki doświadczenia")
plt.savefig("wykres4.png")
plt.show()
