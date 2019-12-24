import csv
import matplotlib.pyplot as plt
import numpy as np


with open("new_data2.csv", "r") as FGM:
    FGM_reader = csv.reader(FGM)
    next(FGM_reader)
    for line in FGM_reader:
        for number in line:
            print(line[0])
