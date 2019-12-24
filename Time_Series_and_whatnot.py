from pandas import Series
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator, AutoLocator, NullFormatter,
                               IndexFormatter, LinearLocator, FixedFormatter)
import csv

data = pd.read_csv('new_data.csv', header=0)

data['time'] = pd.to_datetime(data['time'], yearfirst = True)

'''
print(data.Vswe.dtype)
fig, axes = plt.subplots(nrows=7, ncols=1, sharex=True)
axes[0].set_title('ACE')
axes[0].plot(data['time'], data['Vswe'])
axes[1].plot(data['time'], data['Tswe'])
axes[2].plot(data['time'], data['nswe'])
axes[3].plot(data['time'], data['BmagMFI'])
axes[4].plot(data['time'], data['BxMFI'])
axes[5].plot(data['time'], data['ByMFI'])
axes[6].plot(data['time'], data['BzMFI'])

axes[0].set(ylabel='Vtot (km/s)')
axes[1].set(ylabel='T (K)')
axes[2].set(ylabel='n (cm^(-3))')
axes[3].set(ylabel='Btot (nT)')
axes[4].set(ylabel='Bx (nT)')
axes[5].set(ylabel='By (nT)')
axes[6].set(ylabel='Bz (nT)', xlabel='TIME')

for ax in axes.flat:
    ax.yaxis.set_major_locator(AutoLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.yaxis.set_minor_formatter(NullFormatter())
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.xaxis.set_minor_formatter(NullFormatter())



plt.show()



fig, axes = plt.subplots(nrows=7, ncols=1, sharex=True)
axes[0].set_title('THEMIS-C')

axes[0].plot(data['time'], data['Vmom'])
axes[1].plot(data['time'], data['Tmom'])
axes[2].plot(data['time'], data['nmom'])
axes[3].plot(data['time'], data['BmagFGM'])
axes[4].plot(data['time'], data['BxFGM'])
axes[5].plot(data['time'], data['ByFGM'])
axes[6].plot(data['time'], data['BzFGM'])

axes[0].set(ylabel='Vtot (km/s)')
axes[1].set(ylabel='T (K)')
axes[2].set(ylabel='n (cm^(-3))')
axes[3].set(ylabel='Btot (nT)')
axes[4].set(ylabel='Bx (nT)')
axes[5].set(ylabel='By (nT)')
axes[6].set(ylabel='Bz (nT)')



for ax in axes.flat:
    ax.yaxis.set_major_locator(AutoLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())


    ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.yaxis.set_minor_formatter(NullFormatter())


    ax.xaxis.set_minor_locator(AutoMinorLocator())
   # ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.set(xlabel='TIME')
    

plt.show()



time
Vswe
Tswe
nswe
BmagMFI
BxMFI
ByMFI
BzMFI
Vmom
Tmom
nmom
BmagFGM
BxFGM
ByFGM
BzFGM




data = pd.read_csv('solar_wind.csv', )
distances = pd.read_csv("distances.csv",)

print('meanVswe:  ', np.mean(data.Vswe))
print('meanTswe:  ', np.mean(data.Tswe))
print('meannswe:  ', np.mean(data.nswe))
print('meanBmagMFI:  ', np.mean(data.BmagMFI))
print('meanBxMFI:  ', np.mean(data.BxMFI))
print('meanByMFI:  ', np.mean(data.ByMFI))
print('meanBzMFI:  ', np.mean(data.BzMFI))
print('meanVmom:  ', np.mean(data.Vmom))
print('meanTmom:  ', np.mean(data.Tmom))
print('meannmom:  ', np.mean(data.nmom))
print('meanBmagFGM:  ', np.mean(data.BmagFGM))
print('meanBxFGM:  ', np.mean(data.BxFGM))
print('meanByFGM:  ', np.mean(data.ByFGM))
print('meanBzFGM:  ', np.mean(data.BzFGM))
print('')

print('minVswe:  ', np.min(data.Vswe))
print('minTswe:  ', np.min(data.Tswe))
print('minnswe:  ', np.min(data.nswe))
print('minBmagMFI:  ', np.min(data.BmagMFI))
print('minBxMFI:  ', np.min(data.BxMFI))
print('minByMFI:  ', np.min(data.ByMFI))
print('minBzMFI:  ', np.min(data.BzMFI))
print('minVmom:  ', np.min(data.Vmom))
print('minTmom:  ', np.min(data.Tmom))
print('minnmom:  ', np.min(data.nmom))
print('minBmagFGM:  ', np.min(data.BmagFGM))
print('minBxFGM:  ', np.min(data.BxFGM))
print('minByFGM:  ', np.min(data.ByFGM))
print('minBzFGM:  ', np.min(data.BzFGM))
print('')
print('maxVswe: ', np.max(data.Vswe))
print('maxTswe: ', np.max(data.Tswe))
print('maxnswe: ', np.max(data.nswe))
print('maxBmagMFI: ', np.max(data.BmagMFI))
print('maxBxMFI: ', np.max(data.BxMFI))
print('maxByMFI: ', np.max(data.ByMFI))
print('maxBzMFI: ', np.max(data.BzMFI))
print('maxVmom: ', np.max(data.Vmom))
print('maxTmom: ', np.max(data.Tmom))
print('maxnmom: ', np.max(data.nmom))
print('maxBmagFGM: ', np.max(data.BmagFGM))
print('maxBxFGM: ', np.max(data.BxFGM))
print('maxByFGM: ', np.max(data.ByFGM))
print('maxBzFGM: ', np.max(data.BzFGM))

data["MPAUSEdistance"] = distances["MPAUSEdistance"]
data["BowShockDistance"] = distances["BowShockDistance"]
data["DynamicPressure"] = distances["DynamicPressure"]
data.to_csv("Table_1.csv", index=False)'''
#data.to_excel("Table_1.xlsx", index=False)