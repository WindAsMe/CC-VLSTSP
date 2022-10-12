import random
import numpy as np
from helps import write_tour


name = "as4"
dis = 100
path = "/Users/ISDL/PycharmProjects/CC_VLSTSP/Data/hCC_gLS/best_Dis/"
tour = [0, 1, 2, 3, 0]
Dim = 4
write_tour(path, name, tour, dis, Dim)
