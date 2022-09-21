import time
import numpy as np
import os
import pandas as pd
import helps
from EAs import GA, PSO, hCCGA
from EAs.SA import SimAnneal
from EAs import initial


if __name__ == "__main__":
    data_path = os.path.dirname(os.path.abspath(__file__)) + "/TSP/"

    # tsp_files = ['ics39603.tsp', 'rbz43748.tsp', 'fht47608.tsp', 'fna52057.tsp', 'bna56769.tsp', 'dan59296.tsp',
    #              'sra104815.tsp', 'ara238025.tsp', 'lra498378.tsp',  'lrb744710.tsp']
    # names = ['ics39603', 'rbz43748', 'fht47608', 'fna52057', 'bna56769', 'dan59296', 'sra104815', 'ara238025',
    #          'lra498378', 'lrb744710']
    # scales = [39603, 43748, 47608, 52057, 56769, 59296, 104815, 238025, 498378, 744710]
    tsp_files = ['dbj2924.tsp', 'pia3056.tsp', 'xva2993.tsp']
    names = ['dbj2924', 'pia3056', 'xva2993']
    scales = [2924, 3056, 2993]
    skip = 8
    trial_runs = 20
    NIND = 100
    Max_iter = 500

    for inst in range(len(scales)):
        hCCGA_best_path = os.path.dirname(os.path.abspath(__file__)) + "/Data/hCCGA/best_Dis/" + names[inst] + ".csv"
        hCCGA_time_path = os.path.dirname(os.path.abspath(__file__)) + "/Data/hCCGA/time/" + names[inst] + ".csv"
        cities = helps.read_tsp(data_path + tsp_files[inst], skip)

        for run in range(1):
            CCGA_time_start = time.time()
            best_fitness, best_tour = hCCGA.hCCGA_exe(cities, NIND, Max_iter, sub_size=100, K=50)
            CCGA_time_end = time.time()
            print(best_fitness)
            helps.write_result(hCCGA_time_path, [CCGA_time_end - CCGA_time_start])
            helps.write_result(hCCGA_best_path, [best_fitness])



