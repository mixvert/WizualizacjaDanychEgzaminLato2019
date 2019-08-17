import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("wp.csv", sep=";", index_col=0)
fig, ax1 = plt.subplots()
x = dane.index
ax1.bar(x - 0.2, dane["Budżet"], label="Budżet", width=0.4, color="b")
ax1.set_ylim([90000000, 100000000])
ax1.set_ylabel('Budżet', color='b')
ax1.set_xticks(x)
ax1.set_xlabel("Numer części")
ax2 = ax1.twinx()
plt.title("Budżet i zyski - seria Władca Pierścieni")
ax2.bar(x + 0.2, dane["Zyski"], color="red", label="Zyski", width=0.4)
ax2.set_ylim([800000000, 1200000000])
ax2.set_ylabel("Zyski", color="red")
plt.savefig("wykres5.png")
plt.show()
