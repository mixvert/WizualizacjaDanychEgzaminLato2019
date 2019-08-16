import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("planety.csv", index_col=0)
dane=dane[dane["Masa"]<50000]

plt.pie(dane["Masa"], labels=dane.index, autopct='%1.1f%%', colors=["yellow","orange","red",'royalblue','green','brown'])
plt.title("Masa planet")
plt.text(1,1,"12345")
plt.savefig("wykres4.pdf")
plt.show()