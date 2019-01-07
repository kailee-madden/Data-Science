#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas
from pandas import Series, DataFrame
import numpy as np

D = pandas.read_csv("Dataset-film-data.csv")
    
A = []
C = []
R = []
for index, row in D.iterrows():
    if row["GENRE"] == "ROMANCE":
        R.append(row["AVGRATING_WEBSITE_1"])
    elif row["GENRE"] == "ACTION":
        A.append(row["AVGRATING_WEBSITE_1"])
    elif row["GENRE"] == "COMEDY":
        C.append(row["AVGRATING_WEBSITE_1"])

def average(lst): 
    return sum(lst) / len(lst) 

A_mean = average(A)
C_mean = average(C)
R_mean = average(R)

Genre = ["Action", "Comedy", "Romance"]
Mean = [A_mean, C_mean, R_mean]

def bar(x, y):
    fig, ax = plt.subplots()
    index = np.arange(3)
    bar_width = 0.4
    ax.bar(index, y, bar_width, align = "center")
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(x)
    ax.set_xlabel("Genres")
    ax.set_ylabel("Means")
    plt.savefig("barchart")

barchart = bar(Genre, Mean)