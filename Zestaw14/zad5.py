import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_csv("sport14.csv", sep="#", index_col=0)
men = dane[dane["Płeć"] == "M"]["Popularność"]
women = dane[dane["Płeć"] == "K"]["Popularność"]
X = np.arange(len(men))

plt.bar(X, women, color='orange', label="Kobiety")
plt.bar(X, -men, color='brown', label="Mężczyźni")
plt.title("Popularność sportu")
plt.xticks(X, men.index)
plt.yticks([])
plt.legend()
plt.show()
