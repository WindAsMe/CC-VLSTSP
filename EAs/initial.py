import copy
import random
import numpy as np

import helps


def init_population(indexes, sub_cities, NIND, K=50):
    """
    :param indexes: indexes of cities
    :param sub_cities: coordinates of cities
    :param NIND: population size
    :param K: random chosen city
    :return: generated population
    """

    pop = []
    for i in range(NIND):
        pop.append(K_greedy(indexes, sub_cities, K))
    return np.array(pop)


def K_greedy(indexes, sub_cities, K):
    temp_indexes = copy.deepcopy(indexes)
    tour = [temp_indexes.pop(0)]
    while len(temp_indexes) > 0:
        K = min(K, len(temp_indexes))
        current_city = tour[len(tour) - 1]
        candidate_cities = random.sample(temp_indexes, K)
        next = next_city(current_city, candidate_cities, sub_cities)
        tour.append(temp_indexes.pop(next))
    return tour


def next_city(current, candidates, sub_cities):
    next = 0
    dis = helps.Dis(sub_cities[current], sub_cities[next])
    for i in range(1, len(candidates)):
        new_dis = helps.Dis(sub_cities[current], sub_cities[candidates[i]])
        if new_dis < dis:
            dis = new_dis
            next = i
    return next


def greedy_initial(sub_indexes, sub_cities):
    temp_sub_indexes = copy.deepcopy(sub_indexes)
    route = [temp_sub_indexes.pop(0)]
    current = route[len(route)-1]
    while len(temp_sub_indexes) > 0:
        Distance = []
        for i in range(len(temp_sub_indexes)):
            Distance.append(helps.Dis(sub_cities[current], sub_cities[temp_sub_indexes[i]]))
        next = np.argmin(Distance)
        route.append(temp_sub_indexes.pop(next))
        current = route[len(route) - 1]
    return route