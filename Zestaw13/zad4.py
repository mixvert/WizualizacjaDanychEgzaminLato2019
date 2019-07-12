import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_csv("temp.csv", header=None, index_col=0)
x = np.arange(len(dane.index))

plt.bar(x, dane.iloc[:, 0])
plt.title("Wykres temperatur")
plt.xticks(x, dane.index, rotation=90)
plt.plot([-0.5, 11.5], [0, 0])
plt.tight_layout()
plt.savefig("wykres4.png")
plt.show()
