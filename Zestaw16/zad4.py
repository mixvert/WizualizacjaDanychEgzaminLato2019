import matplotlib.pyplot as plt
import pandas as pd

dane= pd.read_csv("filmy.csv", index_col=0)
plt.title("Popularność filmów")
ex=(0,0,0.1,0,0,0)
plt.pie(dane["Popularność"], explode=ex, labels=dane.index, autopct="%1.f%%", colors=['red', 'orange', 'gold', 'lawngreen', 'lightseagreen', 'royalblue'])
plt.savefig("wykres4.png")
plt.show()