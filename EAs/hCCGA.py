import helps
import math
import geatpy as ea
from EAs.Problem import MyProblem
import numpy as np
from EAs.templet.hCCGA_templet import soea_SEGA_templet
from EAs import initial
from EAs.SA import SimAnneal


def hCCGA_exe(cities, NIND, Max_iter, sub_size=100, K=50):
    labels = helps.K_Nearest(cities, sub_size)
    # helps.draw_city_clustering(cities, labels, "")
    categories = int((len(cities) + sub_size - 1) / sub_size)
    layer = math.ceil(math.log2(categories)) + 1
    iters = helps.iter_allocate(Max_iter, layer)
    sub_indexes = helps.divide_cities(cities, labels)
    elites = []
    best_tour = []
    for i in range(len(sub_indexes)):
        sub_best_tour = initial.greedy_initial(sub_indexes[i], cities)
        elites.append(sub_best_tour)
        best_tour.extend(sub_best_tour)
    best_fitness = helps.tour_Dis(best_tour, cities)

    """The layer of hierarchy"""
    for i in range(layer):
        for j in range(len(elites)):
            best_sub_Dis, best_sub_route = sub_GA(cities, NIND, iters[i], elites[j], K)
            elites[j] = best_sub_route
        centers = []
        for j in range(len(elites)):
            centers.append(helps.centroid(elites[j], cities))
        labels = helps.K_Nearest(centers, 2)
        elites = helps.elites_combine(elites, labels)

        temp_best_tour = helps.list_combine(elites)
        temp_best_fitness = helps.tour_Dis(temp_best_tour, cities)
        print("global best: ", best_fitness)
        print("current best: ", temp_best_fitness)
        if temp_best_fitness < best_fitness:
            best_fitness = temp_best_fitness
            best_tour = temp_best_tour
    return best_fitness, best_tour


def sub_GA(cities, NIND, Max_iter, elite, K):
    """================================实例化问题对象============================"""
    problem = MyProblem(cities, len(elite))  # 生成问题对象
    """==================================种群设置=============================="""
    Encoding = 'P'  # 编码方式，采用排列编码
    Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders)  # 创建区域描述器
    population = ea.Population(Encoding, Field, NIND)  # 实例化种群对象（此时种群还没被初始化，仅仅是完成种群对象的实例化）
    population.Chrom = initial.init_population(elite, cities, NIND, K)
    prophetPop = ea.Population(Encoding, Field, 1)
    prophetPop.Chrom = np.array([elite])

    """================================算法参数设置============================="""
    myAlgorithm = soea_SEGA_templet(problem, population)  # 实例化一个算法模板对象
    myAlgorithm.MAXGEN = Max_iter  # 最大进化代数
    myAlgorithm.mutOper.Pm = 0.8  # 变异概率
    myAlgorithm.logTras = 0  # 设置每隔多少代记录日志，若设置成0则表示不记录日志
    myAlgorithm.verbose = False  # 设置是否打印输出日志信息
    myAlgorithm.drawing = 0  # 设置绘图方式（0：不绘图；1：绘制结果图；2：绘制目标空间过程动画；3：绘制决策空间过程动画）
    """===========================调用算法模板进行种群进化========================"""
    [BestIndi, population] = myAlgorithm.run(prophetPop)  # 执行算法模板，得到最优个体以及最后一代种群
    """==================================输出结果=============================="""
    return BestIndi.ObjV[0], list(BestIndi.Phen[0, :])


