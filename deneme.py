from pandas import Series
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator, AutoLocator, NullFormatter,
                               IndexFormatter, LinearLocator, FixedFormatter)
import csv

'''


x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)
plt.show()

'''
data = pd.read_csv('new_data.csv', header=0)
distances = pd.read_csv("distances.csv",)
data["MPAUSEdistance"] = distances["MPAUSEdistance"]
data["BowShockDistance"] = distances["BowShockDistance"]
data["DynamicPressure"] = distances["DynamicPressure"]
data.to_csv("Table_1.csv", index=False)
data.to_excel("Table_1.xlsx", index=False)



