import geatpy as ea
import numpy as np
import helps


class MyProblem(ea.Problem):  # 继承Problem父类
    def __init__(self, places, indexes):
        name = 'MyProblem'  # 初始化name（函数名称，可以随意设置）
        M = 1  # 初始化M（目标维数）
        maxormins = [1]  # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        Dim = len(places) # 初始化Dim（决策变量维数）
        varTypes = [1] * Dim  # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [1] * Dim  # 决策变量下界
        ub = [Dim] * Dim  # 决策变量上界
        lbin = [1] * Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1] * Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)
        # 新增一个属性存储旅行地坐标
        self.places = np.array(places)
        self.indexes = np.array(indexes)

    def aimFunc(self, pop):  # 目标函数
        X = pop.Phen.copy()  # 得到决策变量矩阵
        size = len(self.indexes)
        ObjV = []  # 存储所有种群个体对应的总路程
        for x in X:
            final_index = int(np.where(self.indexes == (x[size-1]))[0])
            distance = helps.Dis(self.places[0], self.places[final_index])
            current = 0
            for j in range(1, size):
                next = int(np.where(self.indexes == (x[j]))[0])
                distance += helps.Dis(self.places[current], self.places[next])
                current = next
            ObjV.append(distance)
        pop.ObjV = np.array([ObjV]).T
