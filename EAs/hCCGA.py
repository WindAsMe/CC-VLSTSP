import helps
import math
import geatpy as ea
from EAs.Problem import MyProblem
import numpy as np
from EAs.templet.hCCGA_templet import soea_SEGA_templet
import benchmark
from EAs.greedyLS import gLS


def hCCGA_exe(cities, knownTour, Max_iter, func, sub_size=100):

    categories = int((len(cities) + sub_size - 1) / sub_size)
    best_Dis = func(knownTour, cities)
    best_tour = knownTour
    layer = math.ceil(math.log2(categories)) + 1
    sub_tours = helps.divide_cities(knownTour, categories, sub_size)
    print("initial Dis: ", best_Dis)
    """The layer of hierarchy"""
    for i in range(layer):
        for j in range(len(sub_tours)):
            sub_tours[j] = gLS(cities, sub_tours[j], func, Max_iter, 100)
        sub_tours = helps.subtour_merge(sub_tours)
        temp_tour = helps.tour_combine(sub_tours)
        temp_Dis = func(temp_tour, cities)
        if temp_Dis < best_Dis:
            best_Dis = temp_Dis
            best_tour = temp_tour
        print("best Dis: ", best_Dis)

    return best_Dis, best_tour




