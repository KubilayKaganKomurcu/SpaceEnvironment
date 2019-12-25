import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator, AutoLocator, NullFormatter,
                               IndexFormatter, LinearLocator, FixedFormatter)
import csv




data = pd.read_csv('Table_1.csv', header=0)

data['time'] = pd.to_datetime(data['time'], yearfirst = True)

#plt.scatter(data['MPAUSEdistance'], data['DynamicPressure'])
#plt.xlabel('Magnetopause Distance (Re)')
#plt.ylabel('Dynamic Pressure (nPa)')

plt.scatter(data['BowShockDistance'], data['DynamicPressure'],)
plt.xlabel('Bow Shock Distance (Re)')
plt.ylabel('Dynamic Pressure (nPa)')
plt.show()