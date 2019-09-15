import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("dosw30.csv")

plt.plot(dane["Czas"], dane["Zmienna"], color="green", label="Zmienna", linestyle="dashed")
plt.legend(loc=8)
plt.ylabel("Zmienna")
plt.xlabel("Czas")
plt.title("Wyniki doświadczenia")
plt.savefig("wykres4.pdf")
plt.show()
