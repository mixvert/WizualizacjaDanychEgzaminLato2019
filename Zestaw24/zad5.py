import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("medale.csv")
zloto = data["Złote"]
srebro = data["Srebrne"]
braz = data["Brązowe"]
x = np.arange(2)

plt.bar(x, zloto, width=0.25, color="gold", label="Złote")
plt.bar(x + 0.25, srebro, width=0.25, color="silver", label="Srebrne")
plt.bar(x + 0.5, braz, width=0.25, color="brown", label="Brązowe")
plt.ylim([0, 10])
plt.title("Medale Polaków na olimpiadach")
plt.xticks(x + 0.25, data["Olimpiada"])
plt.legend()
plt.show()
