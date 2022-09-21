import copy
import random
import numpy as np

import helps


def init_population(indexes, cities, NIND, K=50):
    """
    :param indexes: indexes of cities
    :param cities: coordinates of cities
    :param NIND: population size
    :param K: random chosen city
    :return: generated population
    """
    pop = []
    for i in range(NIND):
        pop.append(K_greedy(indexes, cities, K))
    return np.array(pop)


def K_greedy(sub_indexes, cities, K):
    temp_indexes = copy.deepcopy(sub_indexes)
    tour = [temp_indexes.pop(0)]
    while len(temp_indexes) > 0:
        current = tour[len(tour) - 1]
        K = min(K, len(temp_indexes))
        candidates = random.sample(temp_indexes, K)
        next = next_city(current, candidates, cities)
        tour.append(next)
        temp_indexes.remove(next)
    return tour


def next_city(current, candidates, cities):
    next = candidates[0]
    dis = helps.Dis(cities[current], cities[next])
    for i in range(1, len(candidates)):
        new_dis = helps.Dis(cities[current], cities[candidates[i]])
        if new_dis < dis:
            dis = new_dis
            next = candidates[i]
    return next


def greedy_initial(sub_indexes, sub_cities):
    temp_sub_indexes = copy.deepcopy(sub_indexes)
    route = [temp_sub_indexes.pop(0)]
    while len(temp_sub_indexes) > 0:
        current = route[len(route) - 1]
        Distance = []
        for i in range(len(temp_sub_indexes)):
            Distance.append(helps.Dis(sub_cities[current], sub_cities[temp_sub_indexes[i]]))
        next = np.argmin(Distance)
        route.append(temp_sub_indexes.pop(next))
    return route