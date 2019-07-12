import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_csv("sport12.csv", sep="#", index_col=0)
men = dane[dane["Płeć"] == "M"]["Popularność"]
women = dane[dane["Płeć"] == "K"]["Popularność"]
X = np.arange(len(men))

plt.barh(X, women, color='red', label="Kobiety")
plt.barh(X, -men, color='blue', label="Mężczyźni")
plt.title("Popularność sportu")
plt.yticks(X, men.index)
plt.xticks([])
plt.legend()
plt.show()
