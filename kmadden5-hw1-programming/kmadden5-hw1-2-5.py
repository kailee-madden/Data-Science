#!/usr/bin/env python3
import pandas
from pandas import Series, DataFrame
import numpy as np 
import pylab 
import scipy.stats as stats

D = pandas.read_csv("Dataset-film-data.csv")

measurements = np.random.normal(D["AVGRATING_WEBSITE_1"].values, D["AVGRATING_WEBSITE_3"].values) 
stats.probplot(measurements, dist="norm", plot=pylab)
pylab.savefig("QQ-Plot")