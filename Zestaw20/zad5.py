import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sklepy.csv", index_col=0)
rok16 = data[data["Rok"] == 2016]["Liczba obiektów"]
x = np.arange(len(rok16))
plt.bar(x, rok16)
plt.title("Rodzaje sklepów w Olsztynie w 2016 r.")
plt.xticks(x, rok16.index)
plt.show()
