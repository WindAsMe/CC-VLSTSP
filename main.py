import time
import numpy as np
import os
import pandas as pd
import helps
from EAs import GA, PSO
import warnings


if __name__ == "__main__":
    data_path = os.path.dirname(os.path.abspath(__file__)) + "/TSP/"

    # tsp_files = os.listdir(data_path)
    # tsp_files = ['ics39603.tsp', 'rbz43748.tsp', 'fht47608.tsp', 'fna52057.tsp', 'bna56769.tsp', 'dan59296.tsp',
    #              'sra104815.tsp', 'ara238025.tsp', 'lra498378.tsp',  'lrb744710.tsp']
    # names = ['ics39603', 'rbz43748', 'fht47608', 'fna52057', 'bna56769', 'dan59296', 'sra104815', 'ara238025',
    #          'lra498378', 'lrb744710']
    # scales = [39603, 43748, 47608, 52057, 56769, 59296, 104815, 238025, 498378, 744710]
    tsp_files = ['xqf131.tsp']
    names = ['xqf131']
    scales = [131]
    skip = 8
    trial_runs = 30
    NIND = 10
    Max_iter = 50
    for run in range(1):
        for inst in range(1):
            GA_time_path = os.path.dirname(os.path.abspath(__file__)) + "/Data/GA/time/" + names[inst] + ".csv"
            GA_best_path = os.path.dirname(os.path.abspath(__file__)) + "/Data/GA/best_Dis/" + names[inst] + ".csv"
            GA_route_path = os.path.dirname(os.path.abspath(__file__)) + "/Data/GA/Route/" + names[inst] + ".csv"
            GA_trace_path = os.path.dirname(os.path.abspath(__file__)) + "/Data/GA/trace/" + names[inst] + ".csv"

            PSO_time_path = os.path.dirname(os.path.abspath(__file__)) + "/Data/PSO/time/" + names[inst] + ".csv"
            PSO_best_path = os.path.dirname(os.path.abspath(__file__)) + "/Data/PSO/best_Dis/" + names[inst] + ".csv"
            PSO_route_path = os.path.dirname(os.path.abspath(__file__)) + "/Data/PSO/Route/" + names[inst] + ".csv"
            PSO_trace_path = os.path.dirname(os.path.abspath(__file__)) + "/Data/PSO/trace/" + names[inst] + ".csv"

            cities = helps.read_tsp(data_path + tsp_files[inst], skip)
            """Conventional GA and PSO"""

            time_GA_start = time.time()
            best_Dis_GA, Route_GA, trace_GA = GA.GA_exe(cities, NIND, Max_iter)
            helps.write_result(GA_best_path, best_Dis_GA)
            helps.write_result(GA_route_path, Route_GA)
            helps.write_result(GA_trace_path, trace_GA)
            time_GA_end = time.time()
            helps.write_result(GA_time_path, [time_GA_end - time_GA_start])
            print("GA run time: ", time_GA_end - time_GA_start)

            time_PSO_start = time.time()
            best_Dis_PSO, Route_PSO, trace_PSO = PSO.PSO_exe(cities, NIND, Max_iter)
            helps.write_result(PSO_best_path, best_Dis_PSO)
            helps.write_result(PSO_route_path, Route_PSO)
            helps.write_result(PSO_trace_path, trace_PSO)
            time_PSO_end = time.time()
            helps.write_result(PSO_time_path, [time_PSO_end - time_PSO_start])
            print("PSO run time: ", time_PSO_end - time_PSO_start)

