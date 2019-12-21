import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import csv


with open("new_data.csv", "r") as Big_data:
    Big_data_reader = csv.reader(Big_data)





    Vswe = []
    Tswe = []
    nswe = []
    BmagMFI = []
    BxMFI = []
    ByMFI = []
    BzMFI = []
    Vmom = []
    Tmom = []
    nmom = []
    BmagFGM = []
    BxFGM = []
    ByFGM = []
    BzFGM = []
    TimeData = []
    for row in Big_data_reader:
        TimeData.append(row[0])
        Vswefloat = float(row[1])
        Tswefloat = float(row[2])
        nswefloat = float(row[3])
        BmagMFIfloat = float(row[4])
        BxMFIfloat = float(row[5])
        ByMFIfloat = float(row[6])
        BzMFIfloat = float(row[7])
        Vmomfloat = float(row[8])
        Tmomfloat = float(row[9])
        nmomfloat = float(row[10])
        BmagFGMfloat = float(row[11])
        BxFGMfloat = float(row[12])
        ByFGMfloat = float(row[13])
        BzFGMfloat = float(row[14])

        Vswe.append(Vswefloat)
        Tswe.append(Tswefloat)
        nswe.append(nswefloat)
        BmagMFI.append(BmagMFIfloat)
        BxMFI.append(BxMFIfloat)
        ByMFI.append(ByMFIfloat)
        BzMFI.append(BzMFIfloat)
        Vmom.append(Vmomfloat)
        Tmom.append(Tmomfloat)
        nmom.append(nmomfloat)
        BmagFGM.append(BmagFGMfloat)
        BxFGM.append(BxFGMfloat)
        ByFGM.append(ByFGMfloat)
        BzFGM.append(BzFGMfloat)
    print(np.max(BmagMFI))
    print(np.max(BxMFI))
    print(np.max(ByMFI))
    print(np.max(BzMFI))
    print(np.min(BmagMFI))
    print(np.min(BxMFI))
    print(np.min(ByMFI))
    print(np.min(BzMFI))

    fig = plt.figure()
    ax1 = fig.add_axes([0.1, 0.04, 0.25, 0.25],
                       xticklabels=[], ylim=(-3, 2))
    ax2 = fig.add_axes([0.1, 0.27, 0.25, 0.25],
                       ylim=(-3, 2))
    ax3 = fig.add_axes([0.1, 0.50, 0.25, 0.25],
                       xticklabels=[], ylim=(-3, 2))
    ax4 = fig.add_axes([0.1, 0.73, 0.25, 0.25],
                       ylim=(0, 2))

    x = TimeData
    ax1.plot(BxMFI)
    ax2.plot(ByMFI)
    ax3.plot(BzMFI)
    ax4.plot(BmagMFI)

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
