import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv("wyksz.csv")

wyzsze = dane[dane["Wykształcenie"] == "wyższe"]
srednie = dane[dane["Wykształcenie"] == "średnie"]
podst = dane[dane["Wykształcenie"] == "podstawowe"]
x = np.arange(3)

plt.subplot(3, 1, 1)
plt.title("Wykształcenie wyższe a wiek")
plt.xticks([0, 1, 2], wyzsze["Wiek"])
plt.ylabel("Liczebność")
plt.bar(x, wyzsze["Liczebność"], width=0.5, label="wyższe", color="blue")
plt.subplot(3, 1, 2)
plt.title("Wykształcenie średnie a wiek")
plt.bar(x, srednie["Liczebność"], width=0.5, label="policealne", color="brown")
plt.xticks([0, 1, 2], wyzsze["Wiek"])
plt.ylabel("Liczebność")
plt.subplot(3, 1, 3)
plt.title("Wykształcenie podstawowe a wiek")
plt.bar(x, podst["Liczebność"], width=0.5, label="srednie", color="green")
plt.xticks([0, 1, 2], wyzsze["Wiek"])
plt.ylabel("Liczebność")
plt.show()
