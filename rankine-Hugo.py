import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


data1 = pd.read_csv('hugo sheath.csv')
data2 = pd.read_csv('hugo sw.csv')

print(data1.mean(axis = 0))
print('')
print(data2.mean(axis = 0))




def sound_speed(Temperature, gamma=5 / 3):
    k = 1.38 * 10 ** (-23)
    mp = 1.67 * 10 ** (-27)  # kg
    return np.sqrt(gamma * k * Temperature / mp)


def mach_number(Temperature, Velocity, gamma=5 / 3):
    k = 1.38 * 10 ** (-23)
    mp = 1.67 * 10 ** (-27)  # kg
    Sound_Speed = np.sqrt(gamma * k * Temperature / mp)
    Velocity = Velocity * 1000
    return Velocity / Sound_Speed

print(sound_speed(7.468260e+06))
print(mach_number(7.468260e+06, 1.644920e+02))
print('')
print(sound_speed(6.146302e+06))
print(mach_number(6.146302e+06, 4.441603e+02 ))