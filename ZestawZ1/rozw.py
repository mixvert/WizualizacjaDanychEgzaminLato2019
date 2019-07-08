import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("prog.csv", index_col=0)
data2 = data.sort_values(["Rok"], ascending=True)

rok18 = data2[data2["Rok"] == 2018].sort_index()
rok19 = data2[data2["Rok"] == 2019].sort_index()

wyn = rok19.iloc[:, 1] - rok18.iloc[:, 1]
pop = rok19.iloc[:, 2] - rok18.iloc[:, 2]

x = np.arange(len(wyn))

plt.bar(x, wyn, width=0.33, label="Wynagrodzenia w $")
plt.title("Wykres zmian 2019 do 2018")
plt.bar(x + 0.33, pop, width=0.33, label="Popularność")
plt.xlabel("Języki programowania")
plt.axhline(color='black')
indeksy = wyn.index
plt.xticks(x + 0.33, indeksy)
plt.annotate("12345", [0, 3])
plt.legend()
plt.show()
