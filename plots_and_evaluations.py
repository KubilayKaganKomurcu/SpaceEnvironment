import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import csv


def magnetopause_distance(n, V):
    mp = 1.67 * 10 ** (-27)
    B_0 = 0.36  # (gauss)
    nu_0 = 4 * np.pi * 10 ** (-7)
    return ((B_0 ** 2) / (nu_0 * mp * n * V ** 2)) ** (1 / 6)


def BowShock_distance(R_mp, gamma=5/3):
    return 1.1*(gamma-1)/(gamma+1)*R_mp


def dynamic_pressure(n, V):
    mp = 1.67 * 10 ** (-27)
    n = n * 10 ** 6
    return 0.5 * n * mp * V ** 2


def eV_to_Kelvin(Temperature):
    return Temperature * 11600
