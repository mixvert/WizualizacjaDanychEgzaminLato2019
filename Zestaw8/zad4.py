import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("przepis.csv", index_col=1)
skladniki = data.index
waga = data["Waga w g"]

plt.pie(waga, labels=skladniki, autopct='%1.0f%%', startangle=180)
plt.savefig('wykres.png', facecolor='w', orientation='portrait')
plt.title('Udział składników w przepisie')
plt.savefig("wykres4.pdf")
plt.show()
