import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_csv("medale.csv", sep=";", index_col=0)
suma = dane["Złote"] + dane["Srebrne"] + dane["Brązowe"]
letnie = suma[dane["Rodzaj"] == "Letnie"]
zimowe = suma[dane["Rodzaj"] == "Zimowe"]
x = np.arange(len(letnie))

plt.subplot(2, 1, 2)
plt.bar(x, letnie, color="orange")
plt.xticks(x, letnie.index)
plt.yticks([0, 5, 10, 15])
plt.title("Medale Polski - letnie olimpiady")
plt.subplot(2, 1, 1)
plt.bar(x, zimowe)
plt.xticks(x, zimowe.index)
plt.yticks([0, 5, 10, 15])
plt.title("Medale Polski - zimowe olimpiady")
plt.show()
