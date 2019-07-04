import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv("rocky.csv", index_col=0)
x = np.arange(len(dane.index))

plt.barh(x, dane["Zyski w mln $"], color="brown")
plt.yticks(x, dane.index)
plt.title("Zyski serii Rocky")
plt.xlabel("Mln $")
plt.ylabel("Nazwa części")
plt.savefig("Wykres4.png")
plt.show()
