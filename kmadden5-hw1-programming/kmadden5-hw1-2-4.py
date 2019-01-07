#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas
from pandas import Series, DataFrame

D = pandas.read_csv("Dataset-film-data.csv")

romance1 =[]
romance2 = []
comedy1 = []
comedy2 = []
action1 = []
action2 = []

for index, row in D.iterrows():
    if row["GENRE"] == "ROMANCE":
        romance1.append(row["AVGRATING_WEBSITE_1"])
        romance2.append(row["AVGRATING_WEBSITE_3"])
    elif row["GENRE"] == "ACTION":
        action1.append(row["AVGRATING_WEBSITE_1"])
        action2.append(row["AVGRATING_WEBSITE_3"])
    else:
        comedy1.append(row["AVGRATING_WEBSITE_1"])
        comedy2.append(row["AVGRATING_WEBSITE_3"])

plt.scatter(romance1, romance2, c="red", marker="o")
plt.scatter(action1, action2, c="blue", marker="*")
plt.scatter(comedy1, comedy2, c="green", marker="D")

plt.savefig("scatterplot")