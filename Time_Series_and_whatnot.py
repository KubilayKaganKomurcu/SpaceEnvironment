from pandas import Series
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,AutoMinorLocator, AutoLocator, NullFormatter, IndexFormatter,LinearLocator, FixedFormatter)

data = pd.read_csv('new_data.csv', header=0)

data['time'] = pd.to_datetime(data['time'], yearfirst = True)
print(data.Vswe.dtype)
fig, axes = plt.subplots(nrows=7, ncols=1, sharex=True)
axes[0].set_title('ACE')
data.groupby(data.time.dt.hour).Vswe.plot(ax=axes[0])
data.groupby(data.time.dt.hour).Tswe.plot(ax=axes[1])
data.groupby(data.time.dt.hour).nswe.plot(ax=axes[2])
data.groupby(data.time.dt.hour).BmagMFI.plot(ax=axes[3])
data.groupby(data.time.dt.hour).BxMFI.plot(ax=axes[4])
data.groupby(data.time.dt.hour).ByMFI.plot(ax=axes[5])
data.groupby(data.time.dt.hour).BzMFI.plot(ax=axes[6])
axes[0].set(ylabel='Vtot (km/s)')
axes[1].set(ylabel='T (K)')
axes[2].set(ylabel='n (cm^(-3))')
axes[3].set(ylabel='Btot (nT)')
axes[4].set(ylabel='Bx (nT)')
axes[5].set(ylabel='By (nT)')
axes[6].set(ylabel='Bz (nT)')






for ax in axes.flat:
    timelist = ['20.00', '21.00', '22.00', '23.00', '00.00', '01.00']
    ax.yaxis.set_major_locator(AutoLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.yaxis.set_minor_formatter(NullFormatter())
    ax.xaxis.set_major_locator(LinearLocator(6))
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.xaxis.set_major_formatter(FixedFormatter(timelist))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.set(xlabel='TIME')


plt.show()


'''

axs[0, 1].plot(x, y, 'tab:orange')
axs[0, 1].set_title('Axis [0,1]')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].set_title('Axis [1,0]')
axs[1, 1].plot(x, -y, 'tab:red')
axs[1, 1].set_title('Axis [1,1]')'''
'''data.groupby(data.time.dt.hour).Vmom.plot()
data.groupby(data.time.dt.hour).Tmom.plot()
data.groupby(data.time.dt.hour).nmom.plot()
data.groupby(data.time.dt.hour).BmagFGM.plot()
data.groupby(data.time.dt.hour).BxFGM.plot()
data.groupby(data.time.dt.hour).ByFGM.plot()
data.groupby(data.time.dt.hour).BzFGM.plot()'''























# df.groupby(['BxMFI']).mean().sort_values('ByMFI', ascending=False)
# newdataframe.reset_index(drop=True, inplace=True)
# print(type(data))
# print(data.head())


# for index, row in data.iterrows():
# print(index, row['BxMFI'])
