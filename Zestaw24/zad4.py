import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("tv.csv", index_col=0)
plt.pie(data, explode=[0.05, 0.05, 0.05, 0, 0, 0, 0, 0, 0, 0], labels=data.index, autopct='%1.1f%%')
plt.title("Oglądalność w 2016 roku")
plt.savefig("Wykres4.pdf")
plt.show()
