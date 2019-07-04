import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("dosw6.csv", sep=";")
plt.plot(dane["Czas"], dane["Zmienna"], linestyle="-.", color="red", label="Zmienna")
plt.legend()
plt.xlim(2, 8)
plt.ylim(9, 12)
plt.xlabel("Czas")
plt.annotate("12345", [7, 9.2])
plt.title("Wyniki doświadczenia")
plt.savefig("Wykres4.png")
plt.show()
