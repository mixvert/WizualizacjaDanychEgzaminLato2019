import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("dosw15.csv", sep=";")
x = dane["Czas"]
y = dane["Zmienna1"]
z = dane["Zmienna2"]

fig, ax1 = plt.subplots()
plt.title("Wykres doświadczenia")
ax1.plot(x, y, 'b.-', label="Zmienna1")
ax2 = ax1.twinx()
ax2.plot(x, z, 'r', label="Zmienna2")
plt.savefig("wykres5.pdf")
plt.show()
