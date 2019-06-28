import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("dosw.csv")

plt.plot(dane["Czas"], dane["Zmienna1"], linestyle="dashed", color="brown", label="Zmienna1")
plt.plot(dane["Czas"], dane["Zmienna2"], linestyle="solid", color="red", label="Zmienna2")
plt.legend(loc="center left")
plt.ylabel("Zmienne")
plt.xticks([2, 3, 4, 5])
plt.yticks([-15, -10, -5, 0])
plt.xlabel("Czas")
plt.grid()
plt.title("Wyniki doświadczenia")
plt.savefig("wykres4.png")
plt.show()
