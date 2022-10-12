import numpy as np
from math import atan2


def tour_Dis(tour, cities):
    size = len(tour)
    dis = Dis(cities[tour[0]], cities[tour[size - 1]])
    for i in range(1, size):
        dis += Dis(cities[tour[i]], cities[tour[i - 1]])
    return int(dis)


def Dis(x, y):
    return np.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


def Geo_Dis(x, y):
    lati = np.pi * x[0] / 180.0
    latj = np.pi * y[0] / 180.0
    longi = np.pi * x[1] / 180.0
    longj = np.pi * y[1] / 180.0
    q1 = np.cos(latj) * np.sin(longi - longj)
    q3 = np.sin((longi - longj) / 2.0)
    q4 = np.cos((longi - longj) / 2.0)
    q2 = np.sin(lati + latj) * q3 * q3 - np.sin(lati - latj) * q4 * q4
    q5 = np.cos(lati - latj) * q4 * q4 - np.cos(lati + latj) * q3 * q3
    return int(6378388.0 * atan2(np.sqrt(q1 * q1 + q2 * q2), q5) + 1.0)


def Geo_tour_Dis(tour, cities):
    size = len(tour)
    dis = Geo_Dis(cities[tour[0]], cities[tour[size - 1]])
    for i in range(1, size):
        dis += Geo_Dis(cities[tour[i]], cities[tour[i - 1]])
    return dis