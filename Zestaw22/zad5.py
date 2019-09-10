import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("ceny.csv", index_col=1)
ryz = data[data["Produkt"] == "Ryż"]["Cena"]
marchew = data[data["Produkt"] == "Marchew"]["Cena"]
x = np.arange(3)

plt.bar(x, ryz, width=0.33, label="Ryż")
plt.bar(x + 0.33, marchew, width=0.33, label="Marchew")
plt.ylim([3, 4.0])
plt.xticks(x + 0.165, data.index)
plt.title("Ceny wybranych produków w 2019 roku")
plt.legend()
plt.show()
