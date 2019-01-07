#!/usr/bin/python3
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    dataset = pd.read_csv("Dataset-clustering.txt", sep="\t")
    dataset.drop(["Win_2015", "Win_2017"], axis=1, inplace=True)
    data_coord = []
    for index, row in dataset.iterrows():
        data_coord.append((dataset["Rank_2015"][index], dataset["Rank_2017"][index]))
    
    centroids = [(1,1), (25,25)]
    kmeans(centroids, data_coord, "scatter-2-1")
    
    return

def kmeans(centroids, data_coord, name):
    red = [] 
    blue = [] 
    for coord in data_coord:
        distance1 = sum([abs(a - b) for a, b in zip(coord, centroids[0])])
        distance2 = sum([abs(a - b) for a, b in zip(coord, centroids[1])])
        if distance1 <= distance2:
            red.append(coord)
        else:
            blue.append(coord)
    centroids_old = centroids

    try:
        center1 = tuple(np.mean(red))
    except:
        center1 = centroids_old[0]
    try:
        center2 = tuple(np.mean(blue))
    except:
        center2 = centroids_old[1]
    centroids_new = [center1, center2]

    check = False
    while check == False:
        red_new = [] 
        blue_new = [] 
        for coord in data_coord:
            distance1 = sum([abs(a - b) for a, b in zip(coord, centroids_new[0])])
            distance2 = sum([abs(a - b) for a, b in zip(coord, centroids_new[1])])
            if distance1 <= distance2:
                red_new.append(coord)
            else:
                blue_new.append(coord)
        centroids_old = centroids_new
        centroids_new = [tuple(np.mean(red_new, axis=0)), tuple(np.mean(blue_new, axis=0))]

        if red == red_new and blue == blue_new:
            check = True
        red = red_new
        blue = blue_new

    red_x = []
    red_y = []
    for data in red:
        x, y = data
        red_x.append(x)
        red_y.append(y)
    blue_x = []
    blue_y = []
    for data in blue:
        x, y = data
        blue_x.append(x)
        blue_y.append(y)   

    plt.scatter(red_x, red_y, c="red")
    plt.scatter(blue_x, blue_y, c="blue")
    plt.scatter(centroids_new[0][0], centroids_new[0][1], c="red", marker="*")
    plt.scatter(centroids_new[1][0], centroids_new[1][1], c="blue", marker="*")
    plt.title('K-Means Plot')
    plt.savefig(name)
    return

if __name__ == "__main__":
    main()