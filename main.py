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
    # tsp_files = ['xrh24104.tsp', 'bbz25234.tsp', 'irx28268.tsp', 'fyg28534.tsp', 'icx28698.tsp', 'boa28924.tsp',
    #             'pbh30440.tsp', 'xib32892.tsp', 'fry33203.tsp', 'bby34656.tsp', 'pba38478.tsp', 'ics39603.tsp',
    #             'rbz43748.tsp', 'fht47608.tsp', 'fna52057.tsp', 'bna56769.tsp', 'dan59296.tsp', 'sra104814.tsp',
    #             'ara238025.tsp', 'lra498378.tsp']
    #
    # names = ['xrh24104', 'bbz25234', 'irx28268', 'fyg28534', 'icx28698', 'boa28924', 'pbh30440', 'xib32892', 'fry33203',
    #          'bby34656', 'pba38478', 'ics39603', 'rbz43748', 'fht47608', 'fna52057', 'bna56769', 'dan59296', 'sra1048154',
    #          'ara238025', 'lra498378']
    #
    # scales = [24104, 25234, 28268, 28534, 28698, 28924, 30440, 32892, 33203, 34656, 38478, 39603, 43748, 47608, 52057,
    #           56769, 59296, 104814, 238025, 498378]

    tsp_files = ['dkg813.tsp']
    names = ['dkg813']
    scales = [813]

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



