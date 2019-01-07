#!/usr/bin/python3
import pandas as pd
import math
import numpy as np
import itertools

def main():
    data = pd.read_csv("Dataset-apriori.txt", sep="\t")
    dataset = data.fillna(0)
    minsup = 2

    apriori(dataset, minsup)
    return

def apriori(dataset, minsup):
    f_1 = {}
    for index, row in dataset.iterrows():
        for value in row:
            if value not in f_1:
                f_1[value] = 1
            else:
                f_1[value] += 1
    F_1 = {}
    for symbol, support in f_1.items():
        if symbol == 0:
            continue
        elif support >= minsup:
            F_1[symbol] = support
    k=1
    f_k = F_1
    while len(f_k) != 0:
        print(f_k)
        k+=1
        temp = list(itertools.combinations(F_1, k))
        temp2 = {}
        for index, row in dataset.iterrows():
            for combo in temp:
                check = True
                for c in combo:
                    for value in row:
                        if value != c:
                            check2 = False
                        else:
                            check2 = True
                            break
                    if check2 == False:
                        check = False
                        break
                if check == True:
                    if combo not in temp2:
                        temp2[combo] = 1
                    else:
                        temp2[combo] += 1
        f_k = {}
        for symbol, support in temp2.items():
            if support >= minsup:
                f_k[symbol] = support
    return

def is_nan(x):
    return (x is np.nan or x != x)

if __name__ == "__main__":
    main()