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

    tsp_files = ['ics39603.tsp', 'rbz43748.tsp', 'fht47608.tsp', 'fna52057.tsp', 'bna56769.tsp', 'dan59296.tsp',
                 'sra104815.tsp', 'ara238025.tsp', 'lra498378.tsp',  'lrb744710.tsp']
    names = ['ics39603', 'rbz43748', 'fht47608', 'fna52057', 'bna56769', 'dan59296', 'sra104815', 'ara238025',
             'lra498378', 'lrb744710']
    scales = [39603, 43748, 47608, 52057, 56769, 59296, 104815, 238025, 498378, 744710]
    # tsp_files = ['xqf131.tsp']
    # names = ['xqf131']
    # scales = [131]
    skip = 8
    trial_runs = 25
    NIND = 10
    Max_iter = 100

    for inst in range(1):
        Greedy_best_path = os.path.dirname(os.path.abspath(__file__)) + "/Data/Greedy/best_Dis/" + names[inst] + ".csv"

        cities = helps.read_tsp(data_path + tsp_files[inst], skip)
        adj_matrix = np.zeros((scales[inst], scales[inst]))
        for i in range(len(cities)):
            for j in range(i+1, len(cities)):
                dis = helps.Dis(cities[i], cities[j])
                adj_matrix[i][j] = dis
                adj_matrix[j][i] = dis
        cities_index = list(range(0, len(cities)))
        greedy_tour = initial.greedy_initial(cities_index, adj_matrix)
        best_Greedy = helps.verify_tour(cities, greedy_tour)
        helps.write_result(Greedy_best_path, [best_Greedy])
        # for run in range(1):
        #
        #     """Conventional GA, PSO, SA"""
        #     # GA.GA_exe(cities, NIND, Max_iter)
        #     best_fitness, best_tour = hCCGA.hCCGA_exe(cities, NIND, Max_iter, adj_matrix, sub_size=10)
        #     print(helps.verify_tour(cities, best_tour))
        #     print(best_fitness, best_tour)


