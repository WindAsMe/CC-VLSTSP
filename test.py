import numpy as np
from geatpy import scaling
import os
from Initialization import init_population
import helps


data_path = os.path.dirname(os.path.abspath(__file__)) + "/TSP/xqf131.tsp"
cities = helps.read_tsp(data_path, 8)
label = helps.K_Nearest(cities, 20)
sub_cities, sub_cities_num = helps.divide_cities(cities, label)
adj_matrix = helps.adjacent_matrix(cities)
NIND = 10
print(sub_cities_num[4])
pop = init_population(sub_cities_num[4], adj_matrix, NIND, K=20, strategy="softmax")
print(pop)

Route = []
for i in pop[0]:
    Route.append(cities[i])

helps.draw_tour(Route, "xqf131", dis=None)


