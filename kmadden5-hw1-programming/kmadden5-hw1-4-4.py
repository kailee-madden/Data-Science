#!/usr/bin/env python3

import numpy
import sklearn
from sklearn.preprocessing import normalize
from scipy.sparse.linalg import svds
import pandas
from pandas import Series, DataFrame

A = pandas.read_csv("Zscored_film_data.csv")
Genre = A["GENRE"]
A = A.drop(["GENRE", "FILM_ID", "Unnamed: 0"], axis=1)
array = A.values
U,S,V = svds(array,k=1)

u = sklearn.preprocessing.normalize(numpy.around(U,1), norm="l2", axis=1)
array_transpose = zip(*array)
v = numpy.dot(array_transpose, u)

i=0
while i < 100:
    u = numpy.dot(array, v)
    v = numpy.dot(array, u)
    i += 1

print(u)
print(v)