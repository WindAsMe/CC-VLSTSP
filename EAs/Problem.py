import geatpy as ea
import numpy as np
import helps


class MyProblem(ea.Problem):  # 继承Problem父类
    def __init__(self, places, Dim):
        name = 'MyProblem'  # 初始化name（函数名称，可以随意设置）
        M = 1  # 初始化M（目标维数）
        maxormins = [1]  # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        varTypes = [1] * Dim  # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [1] * Dim  # 决策变量下界
        ub = [Dim] * Dim  # 决策变量上界
        lbin = [1] * Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1] * Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)
        # 新增一个属性存储旅行地坐标
        self.places = np.array(places)

    def aimFunc(self, pop):  # 目标函数
        size = len(pop.Chrom[0])
        ObjV = []  # 存储所有种群个体对应的总路程
        for x in pop.Phen:
            distance = helps.Dis(self.places[x[0]], self.places[x[size-1]])
            # distance = 0
            for j in range(1, size):
                distance += helps.Dis(self.places[x[j]], self.places[x[j-1]])
            ObjV.append(distance)
        pop.ObjV = np.array([ObjV]).T


def index_transform(phen, indexes):
    real_index = []
    for gene in phen:
        real_index.append(int(np.where(indexes == gene)[0]))
    return real_index
