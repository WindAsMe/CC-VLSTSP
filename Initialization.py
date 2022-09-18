import copy

import numpy as np
from geatpy import scaling


def init_population(sub_cities, adj_matrix, NIND, K=20, strategy="softmax"):
    """
    :param sub_cities: real sub_cities indexes
    :param adj_matrix: distance between city i and city j
    :param NIND: population size
    :param K: related cities
    :param strategy: probability calculation strategy (softmax and normal)
    :return: generated population
    """
    pop = []
    for i in range(NIND):
        pop.append(generate_indi(sub_cities, adj_matrix, K, strategy))
    return pop


def generate_indi(sub_cities, adj_matrix, K=20, strategy="softmax"):
    temp_sub_cities = copy.deepcopy(sub_cities)
    tour = [temp_sub_cities.pop(0)]
    while len(temp_sub_cities) > 0:
        current_city = tour[len(tour) - 1]
        dis_order, candidate_order = get_dis_order(adj_matrix, current_city, temp_sub_cities)
        K = min(len(dis_order), K)
        dis_slice = dis_order[:K]
        fitness = linearity_transform(dis_slice)
        candidate_slice = candidate_order[:K]
        if strategy == "normal":
            next = softmax(fitness)
        else:
            next = normal(fitness)
        tour.append(candidate_slice[next])
        temp_sub_cities.remove(candidate_slice[next])
    return tour


def get_dis_order(adj_matrix, city, candidate):
    Dis = []
    for i in candidate:
        Dis.append(adj_matrix[city][i])
    candidate_order = copy.deepcopy(candidate)
    for i in range(len(Dis)):
        for j in range(i+1, len(Dis)):
            if Dis[j] < Dis[i]:
                temp = Dis[j]
                Dis[j] = Dis[i]
                Dis[i] = temp

                temp = candidate_order[j]
                candidate_order[j] = candidate_order[i]
                candidate_order[i] = temp
    return Dis, candidate_order


def linearity_transform(dis):
    dis = np.array(dis).reshape(-1, 1)
    fitness = scaling(dis)
    return fitness[:, 0]


def softmax(fitness):
    deno = 0
    for f in fitness:
        deno += np.exp(f)
    for i in range(len(fitness)):
        fitness[i] = np.exp(fitness[i]) / deno
    a_P = [fitness[0]]
    for i in range(1, len(fitness)):
        a_P.append(a_P[i - 1] + fitness[i])
    r = np.random.rand()
    for i in range(len(a_P)):
        if r < a_P[i]:
            return i


def normal(fitness):
    deno = sum(fitness)
    for i in range(len(fitness)):
        fitness[i] /= deno
    a_P = [fitness[0]]
    for i in range(1, len(fitness)):
        a_P.append(a_P[i-1] + fitness[i])
    r = np.random.rand()
    for i in range(len(a_P)):
        if r < a_P[i]:
            return i


