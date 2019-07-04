import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv("sport6.csv", index_col=0, sep="_")

m = dane[dane["Płeć"] == "M"]
k = dane[dane["Płeć"] == "K"]
x = np.arange(len(k))

plt.subplot(2, 1, 1)
plt.bar(x, m["Popularność"], color="blue")
plt.xticks(x, k.index)
plt.ylim(0, 60)
plt.title("Popularność sport wśród mężczyzn")
plt.subplot(2, 1, 2)
plt.bar(x, k["Popularność"], color="yellow")
plt.xticks(x, k.index)
plt.ylim(0, 60)
plt.title("Popularność sport wśród kobiet")
plt.show()
