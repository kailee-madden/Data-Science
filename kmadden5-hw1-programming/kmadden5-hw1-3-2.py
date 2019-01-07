#!/usr/bin/env python3

import pandas
from pandas import Series, DataFrame

A = pandas.read_csv("Zscored_film_data.csv")

A_12 = A.drop(["AVGRATING_WEBSITE_3_zscore", "AVGRATING_WEBSITE_4_zscore", "FILM_ID", "GENRE", "Unnamed: 0"], axis=1)
A_13 = A.drop(["AVGRATING_WEBSITE_2_zscore", "AVGRATING_WEBSITE_4_zscore", "FILM_ID", "GENRE", "Unnamed: 0"], axis=1)
A_14 = A.drop(["AVGRATING_WEBSITE_2_zscore", "AVGRATING_WEBSITE_3_zscore", "FILM_ID", "GENRE", "Unnamed: 0"], axis=1)
A_23 = A.drop(["AVGRATING_WEBSITE_1_zscore", "AVGRATING_WEBSITE_4_zscore", "FILM_ID", "GENRE", "Unnamed: 0"], axis=1)
A_24 = A.drop(["AVGRATING_WEBSITE_1_zscore", "AVGRATING_WEBSITE_3_zscore", "FILM_ID", "GENRE", "Unnamed: 0"], axis=1)
A_34 = A.drop(["AVGRATING_WEBSITE_1_zscore", "AVGRATING_WEBSITE_2_zscore", "FILM_ID", "GENRE", "Unnamed: 0"], axis=1)

comparisons = [A_12, A_13, A_14, A_23, A_24, A_34]

for comparison in comparisons:
    covariance = comparison.cov()
    print(covariance)