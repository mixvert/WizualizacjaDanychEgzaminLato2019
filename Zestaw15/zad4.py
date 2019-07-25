import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv("rocky.csv", index_col=0)
x = np.arange(len(dane.index))

plt.bar(x, dane["Zyski w mln $"], color="green")
plt.xticks(x, dane.index)
plt.title("Zyski serii Rocky")
plt.ylabel("Mln $")
plt.xlabel("Nazwa części")
plt.savefig("wykres4.pdf")
plt.show()
