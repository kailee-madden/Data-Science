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
    
    scatterplot(data_coord, "scatter-3-1")
    assign_colors_scatter(data_coord, "scatter-3-2")

    centroids = [(9,15), (5,3), (23,12)]
    kmeans(centroids, data_coord, "scatter-3-3")

    return

def scatterplot(data, name):
    x = []
    y = []
    for pair in data:
        x.append(pair[0])
        y.append(pair[1])
    plt.scatter(x,y, c="black")
    plt.title("Scatter Plot")
    plt.savefig(name)
    return

def assign_colors_scatter(data, name):
    red_x = []
    red_y = []
    blue_x = []
    blue_y = []
    green_x = []
    green_y = []
    for pair in data:
        if pair[0] <15 and pair[1] > 10:
            red_x.append(pair[0])
            red_y.append(pair[1])
        elif pair[0] < 10 and pair[1] < 10:
            blue_x.append(pair[0])
            blue_y.append(pair[1])
        else:
            green_x.append(pair[0])
            green_y.append(pair[1])
    plt.scatter(red_x, red_y, c="red")
    plt.scatter(blue_x, blue_y, c="blue")
    plt.scatter(green_x, green_y, c="green")
    plt.title("Color Assigned Scatter Plot")
    plt.savefig(name)
    return

def kmeans(centroids, data_coord, name):
    red = [] #color for centroid1
    blue = [] #color for centroid2
    green = [] #color for centroid3
    for coord in data_coord:
        distance1 = sum([abs(a - b) for a, b in zip(coord, centroids[0])])
        distance2 = sum([abs(a - b) for a, b in zip(coord, centroids[1])])
        distance3 = sum([abs(a - b) for a, b in zip(coord, centroids[2])])
        if distance1 <= distance2 and distance1 <= distance3:
            red.append(coord)
        elif distance2 < distance1 and distance2 <= distance3:
            blue.append(coord)
        else:
            green.append(coord)
    centroids_old = centroids

    try:
        center1 = tuple(np.mean(red))
    except:
        center1 = centroids_old[0]
    try:
        center2 = tuple(np.mean(blue))
    except:
        center2 = centroids_old[1]
    try:
        center3 = tuple(np.mean(green))
    except:
        center3 = centroids_old[2]
    centroids_new = [center1, center2, center3]

    check = False
    while check == False:
        red_new = [] 
        blue_new = [] 
        green_new = []
        for coord in data_coord:
            distance1 = sum([abs(a - b) for a, b in zip(coord, centroids[0])])
            distance2 = sum([abs(a - b) for a, b in zip(coord, centroids[1])])
            distance3 = sum([abs(a - b) for a, b in zip(coord, centroids[2])])
            if distance1 <= distance2 and distance1 <= distance3:
                red_new.append(coord)
            elif distance2 < distance1 and distance2 <= distance3:
                blue_new.append(coord)
            else:
                green_new.append(coord)
        centroids_old = centroids_new
        centroids_new = [tuple(np.mean(red_new, axis=0)), tuple(np.mean(blue_new, axis=0)), tuple(np.mean(green_new, axis=0))]

        if red == red_new and blue == blue_new and green == green_new:
            check = True
        red = red_new
        blue = blue_new
        green = green_new

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
    green_x = []
    green_y = []
    for data in green:
        x, y = data
        green_x.append(x)
        green_y.append(y)   

    plt.scatter(red_x, red_y, c="red")
    plt.scatter(blue_x, blue_y, c="blue")
    plt.scatter(green_x, green_y, c="green")
    plt.scatter(centroids_new[0][0], centroids_new[0][1], c="red", marker="*")
    plt.scatter(centroids_new[1][0], centroids_new[1][1], c="blue", marker="*")
    plt.scatter(centroids_new[2][0], centroids_new[2][1], c="green", marker="*")
    plt.title('K-Means Plot')
    plt.savefig(name)
    return



if __name__ == "__main__":
    main()