import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import csv


with open("new_data.csv", "r") as Big_data:
    Big_data_reader = csv.reader(Big_data)

    for row in Big_data_reader:
        data1 = row[0]
        data5 = row[5]
        data6 = row[6]
        data7 = row[7]
        data4 = row[4]

    fig = plt.figure()
    ax1 = fig.add_axes([0.1, 0.04, 0.25, 0.25],
                       xticklabels=[], ylim=(-1.2, 1.2))
    ax2 = fig.add_axes([0.1, 0.27, 0.25, 0.25],
                       ylim=(-1.2, 1.2))
    ax3 = fig.add_axes([0.1, 0.50, 0.25, 0.25],
                       xticklabels=[], ylim=(-1.2, 1.2))
    ax4= fig.add_axes([0.1, 0.73, 0.25, 0.25],
                       ylim=(-1.2, 1.2))

    x = data1
    ax1.plot(data5)
    ax2.plot(data6)
    ax3.plot(data7)
    ax4.plot(data4)

    plt.show()



def magnetopause_distance(n, V):
    mp = 1.67 * 10 ** (-27) # kg
    B_0 = 0.3 * 10**(-4)  # Tesla
    nu_0 = 4 * np.pi * 10 ** (-7)
    n = n * 10 ** 6 #(m^-3)
    return ((B_0 ** 2) / (nu_0 * mp * n * V ** 2)) ** (1 / 6)


def BowShock_distance(R_mp, gamma=5/3):
    return 1.1*(gamma-1)/(gamma+1)*R_mp


def dynamic_pressure(n, V):
    mp = 1.67 * 10 ** (-27)
    n = n * 10 ** 6
    return 0.5 * n * mp * V ** 2


def eV_to_Kelvin(Temperature):
    return Temperature * 11600
