#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas
from pandas import Series, DataFrame

D = pandas.read_csv("Dataset-film-data.csv")
d = D.hist(column="AVGRATING_WEBSITE_3", bins=10)
d.title("Histogram of Website 3 Avg Ratings")
plt.savefig("histogram")