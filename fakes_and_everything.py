import csv
import matplotlib.pyplot as plt
import numpy as np


with open("new_data2.csv", "r") as FGM:
    FGM_reader = csv.reader(FGM)
    next(FGM_reader)
    time= []
    Vswe= []
    Tswe= []
    nswe= []
    BmagMFI= []
    BxMFI= []
    ByMFI= []
    BzMFI= []
    Vmom= []
    Tmom= []
    nmom= []
    BmagFGM= []
    BxFGM= []
    ByFGM= []
    BzFGM= []
    d_MPAUSE = []
    d_BSHOCK = []
    Pdyn = []

    faketime = []
    fakeVswe = []
    fakeTswe = []
    fakenswe = []
    fakeBmagMFI = []
    fakeBxMFI = []
    fakeByMFI = []
    fakeBzMFI = []
    fakeVmom = []
    fakeTmom = []
    fakenmom = []
    fakeBmagFGM = []
    fakeBxFGM = []
    fakeByFGM = []
    fakeBzFGM = []
    faked_MPAUSE = []
    faked_BSHOCK = []
    fakePdyn = []


    for line in FGM_reader:
        x = line[0]
        x1 = line[1]
        x2 = line[2]
        x3 = line[3]
        x4 = line[4]
        x5 = line[5]
        x6 = line[6]
        x7 = line[7]
        x8 = line[8]
        x9 = line[9]
        x10 = line[10]
        x11 = line[11]
        x12 = line[12]
        x13 = line[13]
        x14 = line[14]
        x15 = line[15]
        x16 = line[16]
        x17 = line[17]

        x1 = float(x1)
        x2 = float(x2)
        x3 = float(x3)
        x4 = float(x4)
        x5 = float(x5)
        x6 = float(x6)
        x7 = float(x7)
        x8 = float(x8)
        x9 = float(x9)
        x10 = float(x10)
        x11 = float(x11)
        x12 = float(x12)
        x13 = float(x13)
        x14 = float(x14)
        x15 = float(x15)
        x16 = float(x16)
        x17 = float(x17)


        fakeVswe.append(x1)
        if len(fakeVswe) == 5:
            data = np.mean(fakeVswe)
            Vswe.append(data)
            fakeVswe = []


        fakeTswe.append(x2)
        if len(fakeTswe) == 5:
            data = np.mean(fakeTswe)
            Tswe.append(data)
            fakeTswe = []

        fakenswe.append(x3)
        if len(fakenswe) == 5:
            data = np.mean(fakenswe)
            nswe.append(data)
            fakenswe = []

        fakeBmagMFI.append(x4)
        if len(fakeBmagMFI) == 5:
            data = np.mean(fakeBmagMFI)
            BmagMFI.append(data)
            fakeBmagMFI = []

        fakeBxMFI.append(x5)
        if len(fakeBxMFI) == 5:
            data = np.mean(fakeBxMFI)
            BxMFI.append(data)
            fakeBxMFI = []

        fakeByMFI.append(x6)
        if len(fakeByMFI) == 5:
            data = np.mean(fakeByMFI)
            ByMFI.append(data)
            fakeByMFI = []

        fakeBzMFI.append(x7)
        if len(fakeBzMFI) == 5:
            data = np.mean(fakeBzMFI)
            BzMFI.append(data)
            fakeBzMFI = []


        fakeVmom.append(x8)
        if len(fakeVmom) == 5:
            data = np.mean(fakeVmom)
            Vmom.append(data)
            fakeVmom = []

        fakeTmom.append(x9)
        if len(fakeTmom) == 5:
            data = np.mean(fakeTmom)
            Tmom.append(data)
            fakeTmom = []

        fakenmom.append(x10)
        if len(fakenmom) == 5:
            data = np.mean(fakenmom)
            nmom.append(data)
            fakenmom = []

        fakeBmagFGM.append(x11)
        if len(fakeBmagFGM) == 5:
            data = np.mean(fakeBmagFGM)
            BmagFGM.append(data)
            fakeBmagFGM = []


        fakeBxFGM.append(x12)
        if len(fakeBxFGM) == 5:
            data = np.mean(fakeBxFGM)
            BxFGM.append(data)
            fakeBxFGM = []


        fakeByFGM.append(x13)
        if len(fakeByFGM) == 5:
            data = np.mean(fakeByFGM)
            ByFGM.append(data)
            fakeByFGM = []


        fakeBzFGM.append(x14)
        if len(fakeBzFGM) == 5:
            data = np.mean(fakeBzFGM)
            BzFGM.append(data)
            fakeBzFGM = []

        faked_MPAUSE.append(x15)
        if len(faked_MPAUSE) == 5:
            data = np.mean(faked_MPAUSE)
            d_MPAUSE.append(data)
            faked_MPAUSE = []

        faked_BSHOCK.append(x16)
        if len(faked_BSHOCK) == 5:
            data = np.mean(faked_BSHOCK)
            d_BSHOCK.append(data)
            faked_BSHOCK = []

        fakePdyn.append(x17)
        if len(fakePdyn) == 5:
            data = np.mean(fakePdyn)
            Pdyn.append(data)
            fakePdyn = []



with open("new_dataaa.csv", "w", newline='') as new_file:
    fieldnames = [ 'Vswe', "Tswe", "nswe", "BmagMFI", "BxMFI", "ByMFI",
                  "BzMFI", "Vmom", "Tmom", "nmom", "BmagFGM", "BxFGM", "ByFGM", "BzFGM",
                  'MPAUSEdistance','BowShockDistance','DynamicPressure']

    writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(50):
        writer.writerow({ 'Vswe': Vswe[i], "Tswe": Tswe[i], "nswe": nswe[i], "BmagMFI": BmagMFI[i],
                         "BxMFI": BxMFI[i], "ByMFI": ByMFI[i], "BzMFI": BzMFI[i], "Vmom": Vmom[i], "Tmom": Tmom[i],
                         "nmom": nmom[i], "BmagFGM": BmagFGM[i], "BxFGM": BxFGM[i], "ByFGM": ByFGM[i], "BzFGM": BzFGM[i],
                        'MPAUSEdistance': d_MPAUSE[i] , 'BowShockDistance': d_BSHOCK[i], 'DynamicPressure': Pdyn[i]
                        })

