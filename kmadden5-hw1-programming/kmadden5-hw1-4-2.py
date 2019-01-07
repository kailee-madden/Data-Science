#!/usr/bin/env python3

from numpy import linalg as LA
import numpy as np
from sklearn.preprocessing import normalize
from scipy.sparse.linalg import svds
import matplotlib.pyplot as plt
import pandas
from pandas import Series, DataFrame

A = pandas.read_csv("Zscored_film_data.csv")
Genre = A["GENRE"]
A = A.drop(["GENRE", "FILM_ID", "Unnamed: 0"], axis=1)
array = A.values

U,S,V = svds(array,k=2)
svdDf = pandas.DataFrame(data = np.around(U,2), columns = ['left singular vector 1', 'left singular vector 2'])
svdDf["GENRE"] = Genre

romance1 =[]
romance2 = []
comedy1 = []
comedy2 = []
action1 = []
action2 = []

for index, row in svdDf.iterrows():
    if row["GENRE"] == "ROMANCE":
        romance1.append(row["left singular vector 1"])
        romance2.append(row["left singular vector 2"])
    elif row["GENRE"] == "ACTION":
        action1.append(row["left singular vector 1"])
        action2.append(row["left singular vector 2"])
    else:
        comedy1.append(row["left singular vector 1"])
        comedy2.append(row["left singular vector 2"])

plt.scatter(romance1, romance2, c="red", marker="o")
plt.scatter(action1, action2, c="blue", marker="*")
plt.scatter(comedy1, comedy2, c="green", marker="D")
plt.savefig("SVD_scatterplot")