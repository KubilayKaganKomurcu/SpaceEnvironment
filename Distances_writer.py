import numpy as np
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


with open("new_data.csv", "r") as GrandData:
    GrandData_reader = csv.reader(GrandData)
    next(GrandData_reader)
    list_d_MP = []
    list_d_BS = []
    list_P_dyn = []

    for line in GrandData_reader:
        V = line[1]
        n = line[3]

        V = float(V)
        n = float(n)

        if abs(V) > 10 ** 10:
            continue
        if abs(n) > 10 ** 10:
            continue

        d_MP = magnetopause_distance(n, V)
        list_d_MP.append(d_MP)

        d_BS = BowShock_distance(d_MP)
        list_d_BS.append(d_BS)

        P_dyn = dynamic_pressure(n, V)
        list_P_dyn.append(P_dyn)

with open("distances.csv", "w") as new_file:
    fieldnames = ['MPAUSEdistance', 'BowShockDistance', "DynamicPressure"]

    writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(len(list_d_BS)):
        writer.writerow({'MPAUSEdistance': list_d_MP[i], 'BowShockDistance': list_d_BS[i],
                         "DynamicPressure": list_P_dyn[i]})