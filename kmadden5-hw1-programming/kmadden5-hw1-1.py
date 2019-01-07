#!/usr/bin/env python3
import pandas
from pandas import Series, DataFrame

D = pandas.read_csv("Dataset-film-data.csv")
A = pandas.read_csv("Dataset-film-data.csv")
A.drop(["AVGRATING_WEBSITE_1", "AVGRATING_WEBSITE_2", "AVGRATING_WEBSITE_3", "AVGRATING_WEBSITE_4"],axis=1,inplace=True)

cols = list(D.columns)
cols.remove("FILM_ID")
cols.remove("GENRE")

def zscore_normalization(df_old, df_new, columns):
    for col in cols:
        col_zscore = col + '_zscore'
        df_new[col_zscore] = (df_old[col] - df_old[col].mean())/df_old[col].std(ddof=0)
    return df_new

A = zscore_normalization(D, A, cols)
A.to_csv("Zscored_film_data.csv")