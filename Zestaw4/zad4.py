import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("dosw4.csv")

plt.scatter(dane["Czas"], dane["Zmienna"], color="blue", label="Zmienna", marker=".")
plt.legend(loc=8)
plt.ylabel("Zmienna")
plt.xlabel("Czas")
plt.title("Wyniki doświadczenia")
plt.savefig("wykres4.pdf")
plt.show()
