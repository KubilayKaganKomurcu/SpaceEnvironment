import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import csv


def magnetopause_distance(n, V):
    mp = 1.67 * 10 ** (-27) # kg
    B_0 = 0.3 * 10**(-4)  # Tesla
    nu_0 = 4 * np.pi * 10 ** (-7)
    n = n * 10 ** 6 #(m^-3)
    return (((B_0 ** 2) / (nu_0 * mp * n * V ** 2)) ** (1 / 6))/6371


def BowShock_distance(R_mp, gamma=5/3):
    return 1.1*(gamma-1)/(gamma+1)*R_mp


def dynamic_pressure(n, V):
    mp = 1.67 * 10 ** (-27)
    n = n * 10 ** 6
    return 0.5 * n * mp * V ** 2


def eV_to_Kelvin(Temperature):
    return Temperature * 11600



data.Vswe
data.Tswe
data.nswe
data.BmagMFI
data.BxMFI
data.ByMFI
data.BzMFI
data.Vmom
data.Tmom
data.nmom
data.BmagFGM
data.BxFGM
data.ByFGM
data.BzFGM
