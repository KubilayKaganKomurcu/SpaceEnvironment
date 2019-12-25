import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def Auroral_Latitude(d_Mpause):
    return np.rad2deg(np.arccos(1/np.sqrt(d_Mpause)))


with open("Table_1.csv", "r") as GrandData:
    GrandData_reader = csv.reader(GrandData)
    next(GrandData_reader)
    list_d_Aurora = []


    for line in GrandData_reader:
        Au = line[16]

        Au = float(Au)


        d_Au = Auroral_Latitude(Au)
        list_d_Aurora.append(d_Au)

data = pd.read_csv('Table_1.csv')
data['d_Aurora'] = list_d_Aurora
print(data.tail(5))
data.to_csv('Table_1.csv', index=False)

plt.scatter(data['d_Aurora'], data['DynamicPressure'])
plt.xlabel('Auroral latitude (degrees)')
plt.ylabel('Dynamic Pressure (nPa)')

#plt.scatter(data['d_Aurora'], data['MPAUSEdistance'])
#plt.xlabel('Auroral latitude (degrees)')
#plt.ylabel('Magnetopause distance (Re)')



plt.show()