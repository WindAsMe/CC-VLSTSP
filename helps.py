import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
from math import atan2


def read_matrix(file_path):
    matrix = []
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_double = [float(i) for i in row]
            matrix.append(row_double)
    return matrix


def read_tsp(file_path, skip):
    df = pd.read_csv(file_path, sep=" ", skiprows=skip, header=None, encoding='utf8')
    city_x = np.array(df[1][0:-1])
    city_y = np.array(df[2][0:-1])
    cities = list(zip(city_x, city_y))
    return cities


def read_bestTour(file_path, skip):
    df = pd.read_csv(file_path, sep=" ", skiprows=skip, header=None, encoding='utf8')
    tour = np.array(list(map(int, np.array(df[0][0:-1])))) - 1
    return list(tour)


def K_Nearest(cities, sub_size):
    size = len(cities)
    num = int(size / sub_size)
    rest = size
    if size % sub_size != 0:
        num += 1
    clusters = np.zeros(size)
    flag = 0
    for i in range(size):
        if clusters[i] != 0:
            continue
        flag += 1
        clusters[i] = flag
        dis = [float("inf")] * size
        for j in range(i + 1, size):
            if clusters[j] == 0:
                dis[j] = Dis(cities[i], cities[j])
        sort_index = np.argsort(dis)
        if rest >= sub_size:
            sort_index = sort_index[0:sub_size - 1]
        else:
            sort_index = sort_index[0:rest - 1]
        for ind in sort_index:
            clusters[ind] = flag
        rest -= sub_size
    return clusters


def Dis(x, y):
    return np.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


def draw_city_clustering(data, label, name):
    font_title = {'size': 18}
    plt.title(name, font_title)
    category = max(label)
    for i in range(1, int(category + 1)):
        sub_data = []
        for j in range(len(data)):
            if label[j] == i:
                sub_data.append(data[j])
        sub_data = np.array(sub_data)
        plt.scatter(sub_data[:, 0], sub_data[:, 1])
    plt.show()


def divide_cities(knownTour, categories, sub_size):
    size = len(knownTour)
    sub_tours = []
    for i in range(categories):
        start = i * sub_size
        end = min((i + 1) * sub_size, size)
        sub_tours.append(knownTour[start:end])
    return sub_tours


def sub_num_real_num(sub_route, real_route):
    Route = []
    for var in sub_route:
        Route.append(real_route[var])
    return Route


def write_result(path, data):
    with open(path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def write_tour(path, name, tour, dis, Dim):
    with open(path + name, 'a') as f:
        f.write("NAME : " + name + "." + str(dis) + ".tour\n")
        f.write("COMMENT : Length = " + str(dis) + ", found by Rui Zhong, Enzhi Zhang, and Masaharu Munetomo\n")
        f.write("TYPE : TOUR\n")
        f.write("DIMENSION : " + str(Dim) + "\n")
        f.write("TOUR_SECTION\n")
        for city in tour:
            f.write(str(city) + "\n")


def draw_tour(Route, name, dis=None):
    Route = np.array(Route)
    plt.plot(Route[:, 0], Route[:, 1], 'o--')
    font_title = {'size': 18}
    plt.title("Elite of" + name, font_title)
    x_title = {'size': 14}
    if dis is not None:
        plt.xlabel("Distance =" + str(dis), x_title)
    plt.show()


def adjacent_matrix(cities):
    size = len(cities)
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(i + 1, size):
            dis = Dis(cities[i], cities[j])
            matrix[i][j] = dis
            matrix[j][i] = dis
    return matrix


def centroid(sub_indexes, cities):
    center = []
    for index in sub_indexes:
        center.append(cities[index])
    center = np.array(center)
    return [np.mean(center[:, 0]), np.mean(center[:, 1])]


def subtour_merge(sub_tours):
    new_tours = []
    size = len(sub_tours)
    for i in range(0, size, 2):
        temp = sub_tours[i]
        if i + 1 < size:
            temp.extend(sub_tours[i+1])
        new_tours.append(temp)
    return new_tours


def tour_combine(matrix):
    combined_list = []
    for row in matrix:
        combined_list.extend(row)
    return combined_list
