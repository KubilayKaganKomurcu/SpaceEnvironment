import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import csv
import pandas as pd
import plotly.express as px



def magnetopause_distance(n, V):
    mp = 1.67 * 10 ** (-27) # kg
    B_0 = 0.3 * 10**(-4)  # Tesla
    nu_0 = 4 * np.pi * 10 ** (-7)
    n = n * 10 ** 6 #(m^-3)
    V = V * 1000

    a =(B_0 ** 2)
    b = (nu_0 * mp * n * V ** 2)
    c = a/b
    d = c**(1/6)
    e = d


    return e


def BowShock_distance(R_mp, gamma=5/3):
    return (1.1*(gamma-1)/(gamma+1)*R_mp) +R_mp


def dynamic_pressure(n, V):
    mp = 1.67 * 10 ** (-27)
    n = n * 10 ** 6
    V = V * 1000
    return (2 * n * mp * V ** 2) * 10**9 # nanoTesla


def eV_to_Kelvin(Temperature):
    return Temperature * 11600


data = pd.read_csv('Table_1.csv',)
data1 = pd.read_csv('data1.csv',)
data2 = pd.read_csv('data2.csv',)

"""
print('meanPdyn:  ', np.mean(data.DynamicPressure))
print('meanVswe:  ', np.mean(data.Vswe))
print('meannswe:  ', np.mean(data.nswe))
print('meanBmagMFI:  ', np.mean(data.BmagMFI))
print('meanBzMFI:  ', np.mean(data.BzMFI))
print('mean_d_MPAUSE:  ', np.mean(data.MPAUSEdistance))
print('mean_d_BSHOCK:  ', np.mean(data.BowShockDistance))
print("")
print('minPdyn:  ', np.min(data.DynamicPressure))
print('minVswe:  ', np.min(data.Vswe))
print('minnswe:  ', np.min(data.nswe))
print('minBmagMFI:  ', np.min(data.BmagMFI))
print('minBzMFI:  ', np.min(data.BzMFI))
print('min_d_MPAUSE:  ', np.min(data.MPAUSEdistance))
print('min_d_BSHOCK:  ', np.min(data.BowShockDistance))
print("")
print('maxPdyn:  ', np.max(data.DynamicPressure))
print('maxVswe:  ', np.max(data.Vswe))
print('maxnswe:  ', np.max(data.nswe))
print('maxBmagMFI:  ', np.max(data.BmagMFI))
print('maxBzMFI:  ', np.max(data.BzMFI))
print('max_d_MPAUSE:  ', np.max(data.MPAUSEdistance))
print('max_d_BSHOCK:  ', np.max(data.BowShockDistance))"""




fig1 = px.line(data1, x = 'BowShockDistance(Re)', y = 'DynamicPressure(nT)', title='BS vs Pdyn')
fig1.show()


fig2 = px.line(data2, x = 'MPAUSEdistance(Re)', y = 'DynamicPressure(nT)', title='MP vs Pdyn')

fig2.show()


