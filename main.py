import time
import numpy as np
from os import path, listdir
import pandas as pd

import benchmark
import helps
from EAs import hCCGA


if __name__ == "__main__":
    data_path = path.dirname(path.abspath(__file__))
    """The fitness of World TSP is not E distance"""
    names = ['sra104815', 'ara238025', 'lra498378', 'lrb744710', 'world']
    Tours = ['sra104815_268786', 'ara238025_618817', 'lra498378_2227522',
             'lrb744710_1715275', 'world_7515755956']
    scales = [104815, 238025, 498378, 744710, 1904711]
    flags = [0, 0, 0, 0, 1]
    trial_runs = 10
    Max_iter = 100

    for inst in range(4, len(scales)):
        if flags[inst] == 0:
            func = benchmark.tour_Dis
        else:
            func = benchmark.Geo_tour_Dis
        hCCGA_best_path = data_path + "/Data/hCC_gLS/best_Dis/" + names[inst] + "/"
        hCCGA_trace_path = data_path + "/Data/hCC_gLS/trace/" + names[inst] + ".csv"
        hCCGA_time_path = data_path + "/Data/hCC_gLS/time/" + names[inst] + ".csv"
        knownTour_path = data_path + "/KnownTour/"
        cities_path = data_path + "/TSP/"

        cities = helps.read_tsp(cities_path + names[inst] + ".tsp", 8)
        knownTour = helps.read_bestTour(knownTour_path + Tours[inst] + ".tour", 5)

        for run in range(2):
            CCGA_time_start = time.time()
            # best_Dis, best_tour, obj_trace = hCCGA.hCCGA_exe(cities, knownTour, Max_iter, func, sub_size=100)
            CCGA_time_end = time.time()
            best_Dis, best_tour, obj_trace = 0, [1,2], [1,2]
            helps.write_result(hCCGA_time_path, [int(CCGA_time_end - CCGA_time_start)])
            helps.write_result(hCCGA_trace_path, obj_trace)
            helps.write_tour(hCCGA_best_path, names[inst], best_tour, best_Dis, scales[inst], run)





