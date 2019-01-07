#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas
from pandas import Series, DataFrame

D = pandas.read_csv("Dataset-film-data.csv")
D.boxplot(column="AVGRATING_WEBSITE_1", by="GENRE")
plt.savefig("boxplot")