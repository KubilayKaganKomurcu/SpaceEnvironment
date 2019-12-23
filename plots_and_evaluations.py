import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import csv



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


