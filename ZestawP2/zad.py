import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("przepis.csv", index_col=1)
plt.pie(data["Waga w g"], explode=[0.05, 0, 0, 0, 0, 0, 0], labels=data.index, autopct='%1.f%%')
plt.title("Udział składników w przepisie")
plt.savefig("zad.png")
plt.show()
