import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("hotele.csv", index_col=0)
plt.pie(data, labels=data.index, autopct='%1.f%%')
plt.title("Hotele wg kategorii w województwie warm.-maz. w 2017 r.")
plt.savefig("wykres4.png")
plt.show()
