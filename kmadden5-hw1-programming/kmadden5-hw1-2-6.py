#!/usr/bin/env python3
import pandas
from pandas import Series, DataFrame
import scipy
from scipy.stats import entropy

D = pandas.read_csv("Dataset-film-data.csv")

def bin_probabilities(bin_1_upper_bound, bin_3_lower_bound,column_name):
    bucket1 = 0
    bucket2 = 0
    bucket3 = 0
    for value in D[column_name]:
        if value < bin_1_upper_bound:
            bucket1 +=1
        elif value >= bin_3_lower_bound:
            bucket3 += 1
        else:
            bucket2 +=1
    p = [bucket1/150.0, bucket2/150.0, bucket3/150.0]
    return p

q = bin_probabilities(4.5, 6, "AVGRATING_WEBSITE_3")
p = bin_probabilities(4.5, 6, "AVGRATING_WEBSITE_1")

print(entropy(p,q))
print(entropy(q,p))