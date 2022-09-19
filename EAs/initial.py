import copy
import random

import numpy as np
from geatpy import scaling


def init_population(sub_cities, adj_matrix, NIND, K=50):
    """
    :param sub_cities: real sub_cities indexes
    :param adj_matrix: distance between city i and city j
    :param NIND: population size
    :param K: random chosen city
    :return: generated population
    """

    pop = []
    for i in range(NIND):
        pop.append(K_greedy(sub_cities, adj_matrix, K))
    return np.array(pop)


def K_greedy(sub_cities, adj_matrix, K):
    temp_sub_cities = copy.deepcopy(sub_cities)
    tour = [temp_sub_cities.pop(0)]
    while len(temp_sub_cities) > 0:
        K = min(K, len(temp_sub_cities))
        current_city = tour[len(tour) - 1]
        candidate_cities = random.sample(temp_sub_cities, K)
        next = next_city(current_city, candidate_cities, adj_matrix)
        tour.append(next)
        temp_sub_cities.remove(next)
    return tour


def next_city(current, candidates, adj_matrix):
    next = candidates[0]
    dis = adj_matrix[current][next]
    for i in range(1, len(candidates)):
        new_dis = adj_matrix[current][candidates[i]]
        if new_dis < dis:
            dis = new_dis
            next = candidates[i]
    return next


def greedy_initial(sub_cities, adj_matrix):
    temp_sub_cities = copy.deepcopy(sub_cities)
    route = [temp_sub_cities[0]]
    temp_sub_cities.remove(temp_sub_cities[0])
    while len(temp_sub_cities) > 0:
        current = route[len(route)-1]
        Distance = []
        for city in temp_sub_cities:
            Distance.append(adj_matrix[city][current])
        next = np.argmin(Distance)
        route.append(temp_sub_cities[next])
        temp_sub_cities.remove(temp_sub_cities[next])
    return route