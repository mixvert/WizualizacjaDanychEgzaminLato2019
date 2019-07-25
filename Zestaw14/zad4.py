import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_csv("dosw14.csv")
plt.scatter(dane["Czas"], dane["Zmienna"], marker='.', color="red", label="Zmienna")
x = np.arange(1, 4, step=0.01)
plt.plot(x, x * np.cos(x) + 0.5, label="Dopasowanie")
plt.legend()
plt.xlabel("Czas")
plt.title("Wykres doświadczenia")
plt.show()
