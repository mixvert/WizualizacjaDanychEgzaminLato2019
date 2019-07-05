import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv("wyksz.csv")
wyzsze = dane[dane["Wykształcenie"] == "wyższe"]
srednie = dane[dane["Wykształcenie"] == "średnie"]
podst = dane[dane["Wykształcenie"] == "policealne"]
x = np.arange(3)

plt.title("Wykształcenie a wiek")
plt.bar(x, wyzsze["Liczebność"], width=0.25, label="wyższe", color="blue")
plt.bar(x + 0.25, podst["Liczebność"], width=0.25, label="policealne", color="brown")
plt.bar(x + 0.5, srednie["Liczebność"], width=0.25, label="srednie", color="green")
plt.xticks([0.25, 1.25, 2.25], wyzsze["Wiek"])
plt.xlabel("Przedział wiekowy")
plt.ylabel("Liczebność")
plt.legend(loc="right")
plt.show()
