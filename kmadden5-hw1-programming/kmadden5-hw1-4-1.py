#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas
from pandas import Series, DataFrame
import sklearn
from sklearn.decomposition import PCA
import numpy as np

A = pandas.read_csv("Zscored_film_data.csv")
Genre = A["GENRE"]
A = A.drop(["GENRE", "FILM_ID"], axis=1)
A = A.drop(["Unnamed: 0"], axis=1) #this is the column that was added when converted into a csv

values = A.values
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(values)
principalDf = pandas.DataFrame(data = principalComponents, columns = ["principal component 1", "principal component 2"])
principalDf["GENRE"] = Genre

romance1 =[]
romance2 = []
comedy1 = []
comedy2 = []
action1 = []
action2 = []

for index, row in principalDf.iterrows():
    if row["GENRE"] == "ROMANCE":
        romance1.append(row["principal component 1"])
        romance2.append(row["principal component 2"])
    elif row["GENRE"] == "ACTION":
        action1.append(row["principal component 1"])
        action2.append(row["principal component 2"])
    else:
        comedy1.append(row["principal component 1"])
        comedy2.append(row["principal component 2"])

plt.scatter(romance1, romance2, c="red", marker="o")
plt.scatter(action1, action2, c="blue", marker="*")
plt.scatter(comedy1, comedy2, c="green", marker="D")

plt.savefig("principal_scatterplot")