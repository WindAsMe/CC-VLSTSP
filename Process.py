import matplotlib.pyplot as plt
import csv
from os import path
import pandas as pd
import numpy as np


def read_csv(path):
    with open(path) as f:
        read = csv.reader(f)
        traces = []
        for row in read:
            trace = []
            for i in range(len(row)):
                trace.append(float(row[i]))
            traces.append(trace)
        return np.array(traces)




def draw_convergence(x, data, name):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.plot(x, data, label='hCC-gLS')
    # plt.semilogy(x, data, label='hCC-gLS')
    font_title = {'size': 18}
    font = {'size': 16}
    plt.title(name, font_title)
    plt.xlabel('Optimization layers', font)
    plt.ylabel('Distance', font)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    names = ['sra104815', 'ara238025', 'lra498378', 'lrb744710', 'world']
    inst = 3
    this_path = path.dirname(path.abspath(__file__)) + "/Data/hCC_gLS/trace/" + names[inst] + ".csv"
    trace = read_csv(this_path)
    trace_mean = np.mean(trace, axis=0)
    print("best: ", np.min(trace[:, len(trace_mean)-1]))
    print(trace_mean)
    x = np.linspace(0, len(trace_mean), len(trace_mean))
    draw_convergence(x, trace_mean, names[inst])