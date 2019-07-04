import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("sport5.csv", index_col=0, sep="#")
m = dane[dane["Płeć"] == "M"]
k = dane[dane["Płeć"] == "K"]

plt.subplot(1, 2, 1)
plt.pie(m["Popularność"], labels=m.index, autopct="%1.f%%")
plt.title("Popularność sport wśród mężczyzn")
plt.subplot(1, 2, 2)
plt.pie(k["Popularność"], labels=k.index, autopct="%1.f%%")
plt.title("Popularność sport wśród kobiet")
plt.show()
