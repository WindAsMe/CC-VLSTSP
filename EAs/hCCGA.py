import helps
import math
import geatpy as ea
from EAs.Problem import MyProblem
import numpy as np
from EAs.templet.hCCGA_templet import soea_SEGA_templet
import benchmark
from EAs.greedyLS import gLS


def hCCGA_exe(cities, knownTour, NIND, Max_iter, func, sub_size=100):

    categories = int((len(cities) + sub_size - 1) / sub_size)
    best_Dis = func(knownTour, cities)
    layer = math.ceil(math.log2(categories)) + 1
    sub_tours = helps.divide_cities(knownTour, categories, sub_size)
    print("initial Dis: ", best_Dis)
    """The layer of hierarchy"""
    for i in range(layer):
        print(len(sub_tours))
        for j in range(len(sub_tours)):
            sub_tours[j] = gLS(cities, sub_tours[j], func, Max_iter)
        sub_tours = helps.subtour_merge(sub_tours)
        temp_tour = helps.tour_combine(sub_tours)
        temp_Dis = func(temp_tour, cities)
        if temp_Dis < best_Dis:
            best_Dis = temp_Dis
            best_tour = temp_tour
        print("best Dis: ", best_Dis)

    #
    #     temp_best_tour = helps.list_combine(elites)
    #     temp_best_fitness = helps.tour_Dis(temp_best_tour, cities)
    #     print("global best: ", best_fitness)
    #     print("current best: ", temp_best_fitness)
    #     if temp_best_fitness < best_fitness:
    #         best_fitness = temp_best_fitness
    #         best_tour = temp_best_tour
    # return best_fitness, best_tour




