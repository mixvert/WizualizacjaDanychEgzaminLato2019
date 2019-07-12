import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("zyski.csv", index_col=0)

plt.plot(dane["Filmy"], linestyle="dashed", color="blue", label="Filmy")
plt.plot(dane["Gry"], linestyle="solid", color="green", label="Gry")
plt.legend(loc="upper left")
plt.ylabel("Zyski")
plt.xticks([0, 1, 2, 3, 4, 5], dane.index)
plt.xlabel("Miesiąc")
plt.ylim(0, 100)
plt.grid()
plt.title("Zyski z filmów i gier")
plt.show()
