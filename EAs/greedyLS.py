import copy
import random
import numpy as np


def gLS(cities, tour, func, Max_iter):
    length = len(tour) - 2
    best_Dis = func(tour, cities)
    best_Tour = tour
    for i in range(Max_iter):
        r1, r2 = 0, 0
        while r1 == r2:
            r1, r2 = random.randint(1, length), random.randint(1, length)
        r1, r2 = min(r1, r2), max(r1, r2)
        temp_tour, temp_Dis = search(cities, tour, r1, r2, func)
        if temp_Dis < best_Dis:
            best_Dis = temp_Dis
            best_Tour = temp_tour
    return best_Tour


def search(cities, tour, r1, r2, func):
    swap_tour = swap(tour, r1, r2)
    swap_Dis = func(swap_tour, cities)
    insert_tour = insert(tour, r1, r2)
    insert_Dis = func(insert_tour, cities)
    inverse_tour = inverse(tour, r1, r2)
    inverse_Dis = func(inverse_tour, cities)
    i = np.argmin([swap_Dis, insert_Dis, inverse_Dis])
    return [swap_tour, insert_tour, inverse_tour][i], [swap_Dis, insert_Dis, inverse_Dis][i]


def swap(tour, i, j):
    temp_tour = copy.deepcopy(tour)
    temp = temp_tour[i]
    temp_tour[i] = temp_tour[j]
    temp_tour[j] = temp
    return temp_tour


def insert(tour, i, j):
    temp_tour = copy.deepcopy(tour)
    temp_tour.insert(i, temp_tour.pop(j))
    return temp_tour


def inverse(tour, i, j):
    temp_tour = copy.deepcopy(tour)
    while i < j:
        temp = temp_tour[i]
        temp_tour[i] = temp_tour[j]
        temp_tour[j] = temp
        i += 1
        j -= 1
    return temp_tour

