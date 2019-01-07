#!/usr/bin/env python3

import pandas
from pandas import Series, DataFrame

D = pandas.read_csv("Dataset-film-data.csv")

D_12 = D.drop(["AVGRATING_WEBSITE_3", "AVGRATING_WEBSITE_4", "FILM_ID", "GENRE"], axis=1)
D_13 = D.drop(["AVGRATING_WEBSITE_2", "AVGRATING_WEBSITE_4", "FILM_ID", "GENRE"], axis=1)
D_14 = D.drop(["AVGRATING_WEBSITE_2", "AVGRATING_WEBSITE_3", "FILM_ID", "GENRE"], axis=1)
D_23 = D.drop(["AVGRATING_WEBSITE_1", "AVGRATING_WEBSITE_4", "FILM_ID", "GENRE"], axis=1)
D_24 = D.drop(["AVGRATING_WEBSITE_1", "AVGRATING_WEBSITE_3", "FILM_ID", "GENRE"], axis=1)
D_34 = D.drop(["AVGRATING_WEBSITE_1", "AVGRATING_WEBSITE_2", "FILM_ID", "GENRE"], axis=1)

comparisons = [D_12, D_13, D_14, D_23, D_24, D_34]

for comparison in comparisons:
    covariance = comparison.cov()
    print(covariance)