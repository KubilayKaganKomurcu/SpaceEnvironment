import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import csv

Vx = []
AceX = [233.44, 233.45, 233.45, 233.45, 233.45, 233.46, 233.46, 233.46, 233.46, 233.46, 233.47, 233.47, 233.47, 233.47,
        233.48, 233.48, 233.48, 233.48, 233.49, 233.49, 233.49, 233.49, 233.50, 233.50, 233.50, 233.50, 233.50, 233.51,
        233.51]

ThemisX = [9.01, 9.03, 9.06, 9.08, 9.10, 9.12, 9.14, 9.16, 9.18, 9.20, 9.23, 9.25, 9.27, 9.29, 9.31, 9.33, 9.35, 9.37,
           9.39, 9.41, 9.44, 9.46, 9.48, 9.50, 9.52, 9.54, 9.56, 9.58, 9.60, 9.62, 9.64, 9.66, 9.68, 9.70, 9.72, 9.74,
           9.76, 9.78, 9.80, 9.82, 9.84, 9.86, 9.88, 9.90, 9.92, 9.94, 9.96, 9.98, 10.00, 10.02, 10.04, 10.06, 10.08,
           10.10, 10.12, 10.14, 10.16, 10.18, 10.20, 10.22, 10.24, 10.26, 10.28, 10.29, 10.31, 10.33, 10.35, 10.37,
           10.39, 10.41, 10.43, 10.45, 10.47, 10.49, 10.50, 10.52, 10.54, 10.56, 10.58, 10.60, 10.62, 10.63, 10.65,
           10.67, 10.69, 10.71, 10.73, 10.75, 10.76, 10.78, 10.80, 10.82, 10.84, 10.86, 10.87, 10.89, 10.91, 10.93,
           10.95, 10.96, 10.98, 11.00, 11.02, 11.04, 11.05, 11.07, 11.09, 11.11, 11.13, 11.14, 11.16, 11.18, 11.20,
           11.21, 11.23, 11.25, 11.27, 11.28, 11.30, 11.32, 11.34, 11.35, 11.37, 11.39, 11.41, 11.42, 11.44, 11.46,
           11.47, 11.49, 11.51, 11.53, 11.54, 11.56, 11.58, 11.59, 11.61, 11.63, 11.64, 11.66, 11.68, 11.69, 11.71,
           11.73, 11.75, 11.76, 11.78, 11.80, 11.81, 11.83, 11.84, 11.86, 11.88, 11.89, 11.91, 11.93, 11.94, 11.96,
           11.98, 11.99, 12.01, 12.02, 12.04, 12.06, 12.07, 12.09, 12.11, 12.12, 12.14, 12.15, 12.17, 12.19, 12.20,
           12.22, 12.23, 12.25, 12.26, 12.28, 12.30, 12.31, 12.33, 12.34, 12.36, 12.37, 12.39, 12.41, 12.42, 12.44,
           12.45, 12.47, 12.48, 12.50, 12.51, 12.53, 12.54, 12.56, 12.58, 12.59, 12.61, 12.62, 12.64, 12.65, 12.67,
           12.68, 12.70, 12.71, 12.73, 12.74, 12.76, 12.77, 12.79, 12.80, 12.82, 12.83, 12.85, 12.86, 12.88, 12.89,
           12.90, 12.92, 12.93, 12.95, 12.96, 12.98, 12.99, 13.01, 13.02, 13.04, 13.05, 13.07, 13.08, 13.09, 13.11,
           13.12, 13.14, 13.15, 13.17, 13.18, 13.19, 13.21, 13.22, 13.24, 13.25, 13.27, 13.28, 13.29, 13.31, 13.32,
           13.34, 13.35, 13.36, 13.38, 13.39, 13.40, 13.42, 13.43, 13.45, 13.46, 13.47, 13.49, 13.50, 13.52, 13.53,
           13.54, 13.56, 13.57, 13.58, 13.60, 13.61, 13.62, 13.64, 13.65, 13.66, 13.68, 13.69, 13.70, 13.72, 13.73,
           13.74, 13.76, 13.77, 13.78, 13.80, 13.81, 13.82, 13.84, 13.85, 13.86, 13.88, 13.89, 13.90, 13.92, 13.93,
           13.94, 13.95, 13.97, 13.98, 13.99, 14.01, 14.02, 14.03, 14.04, 14.06, 14.07, 14.08, 14.09, 14.11, 14.12,
           14.13, 14.15, 14.16, 14.17, 14.18, 14.20, 14.21, 14.22, 14.23, 14.25, 14.26, 14.27, 14.28, 14.30, 14.31,
           14.32, 14.33, 14.34, 14.36, 14.37, 14.38, 14.39, 14.41, 14.42, 14.43, 14.44, 14.45, 14.47, 14.48, 14.49,
           14.50, 14.51, 14.53, 14.54, 14.55, 14.56, 14.57, 14.59]

with open("AC_H0_SWE_95692.csv", "r") as SWEPAM:
    SWEPAM_reader = csv.reader(SWEPAM)
    next(SWEPAM_reader)
    Vx = []
    Vswe = []
    nswe = []
    Tswe = []
    time_swe = []
    for line in SWEPAM_reader:
        t = line[0]
        x = line[1]
        x = float(x)
        if abs(x) > 10 ** 10:
            continue
        nswe.append(x)
        time_swe.append(t)

        y = line[3]
        y = float(y)
        if abs(y) > 10 ** 10:
            continue
        Tswe.append(y)

        z1 = line[4]
        z2 = line[5]
        z3 = line[6]
        z1 = float(z1)
        z2 = float(z2)
        z3 = float(z3)
        z = np.sqrt((z1 ** 2) + (z2 ** 2) + (z3 ** 2))
        if z > 10 ** 10:
            continue
        Vswe.append(z)

        x = line[4]
        x = abs(float(x))
        if x > 6000:
            continue
        Vx.append(x)

    Vx_mean = np.mean(Vx)
    print("mean SW velocity is (km/s):", Vx_mean)
    Vx_mean = 540
    AceXMean = np.mean(AceX)
    ThemisXMean = np.mean(ThemisX)
    Delay_Time = (AceXMean - ThemisXMean) * 6371 / Vx_mean
    print("Delay time is (minutes):", Delay_Time / 60)

# Distance = WindXMean - ThemisXMean
# DelayTime = Distance / 'velocity X'

with open("AC_H0_MFI_95692.csv", "r") as MFI:
    MFI_reader = csv.reader(MFI)
    next(MFI_reader)
    Bmfi = []
    time_fgm = []
    for line in MFI_reader:
        t = line[0]
        x = line[1]
        x = float(x)
        if abs(x) > 10 ** 10:
            continue
        Bmfi.append(x)
        time_fgm.append(t)

with open("THC_L2_FGM_89446.csv", "r") as FGM:
    FGM_reader = csv.reader(FGM)
    next(FGM_reader)
    Bfgm = []
    Bx = []
    By = []
    Bz = []
    time_fgm = []
    for line in FGM_reader:
        t = line[0]
        x = line[1]
        x = float(x)
        if abs(x) > 10 ** 10:
            continue
        Bfgm.append(x)
        time_fgm.append(t)

        x = line[2]
        x = float(x)
        if abs(x) > 10 ** 10:
            continue
        Bx.append(x)

        x = line[3]
        x = float(x)
        if abs(x) > 10 ** 10:
            continue
        By.append(x)

        x = line[4]
        x = float(x)
        if abs(x) > 10 ** 10:
            continue
        Bz.append(x)

with open("THC_L2_MOM_216777.csv", "r") as MOM:
    MOM_reader = csv.reader(MOM)
    next(MOM_reader)
    Vmom = []
    nmom = []
    Tmom = []
    time_mom = []
    for line in MOM_reader:
        t = line[0]
        x = line[1]
        x = float(x)
        if abs(x) > 10 ** 10:
            continue
        nmom.append(x)
        time_mom.append(t)

        z1 = line[5]
        z2 = line[6]
        z3 = line[7]
        z1 = float(z1)
        z2 = float(z2)
        z3 = float(z3)
        y = 11600 * (z1 + z2 + z3) / 3
        if abs(y) > 1000000000000000000:
            continue
        Tmom.append(y)

        z1 = line[2]
        z2 = line[3]
        z3 = line[4]
        z1 = float(z1)
        z2 = float(z2)
        z3 = float(z3)
        z = np.sqrt((z1 ** 2) + (z2 ** 2) + (z3 ** 2))
        if z > 10 ** 10:
            continue
        Vmom.append(z)
#fig1 = go.Figure(data=[go.Table(header=dict(values=["time1", 'magnetic field1', 'temperature1', 'number density1',
 #                                                   'velocity1', ]),
  #                              cells=dict(values=[time_swe, Bmfi, Tswe, nswe, Vswe]))
    #                   ])
#fig1.show()

#fig2 = go.Figure(data=[go.Table(header=dict(values=["time2", 'magnetic field2', 'temperature2',
 #                                                   'number density2', 'velocity2']),
  #                              cells=dict(values=[time_mom, Bfgm, Tmom, nmom, Vmom]))
   #                    ])
#fig2.show()
plt.plot(time_mom, Tmom)
#plt.plot(time_mom, nmom)
#plt.plot(time_mom, Vmom)
#plt.plot(time_fgm, Bfgm)
#plt.plot(time_fgm, Bx)
#plt.plot(time_fgm, By)
#plt.plot(time_fgm, Bz)
plt.show()

