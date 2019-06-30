import json
import numpy as np
import matplotlib.pyplot as plt
# method block
from math import exp
from scipy.stats import expon
import seaborn as sns

sSize = 10000


def ex1():
    data = {}
    vX = expon.rvs(scale=1000, size=sSize)
    TK = np.array([vX[0:i+1].sum(axis=0) / sSize for i in range(sSize)])
    print(max(TK))
    print(TK)
    T_vida = []
    T_vida.append(0)
    T_vida[0] = TK[0]
    T_vida += [TK[i+1]-TK[i] for i in range(sSize-1)]

    data['Tempo de vida - 10º componente'] = T_vida[9]
    data['Tempo de vida - mediana'] = np.median(np.sort(T_vida))
    data['Tempo de vida - media'] = np.mean(np.sort(T_vida))
    data['Tempo de vida - desvio padrão'] = np.std(np.sort(T_vida))
    data['Tempo de vida - variância'] = np.var(np.sort(T_vida))
    data['Tempo de vida - percentil95'] = np.percentile(np.sort(T_vida), 95)

    with open('../../assets/data/ex1.json', 'w') as wJson:
        json.dump(data, wJson, indent=4)
    sns.distplot(T_vida)
    plt.savefig("../../assets/data/Ex1.png")
    plt.clf()
    return vX


def ex2(times):
    data = {}
    alpha = (1/1.05)
    beta = 10
    cost = []
    for i in range(sSize):
        cost.append(beta * exp(-1 * alpha * (times[i]/(8760))))

    data['Custo de manutenção - 10º componente'] = cost[9]
    data['Custo de manutenção - media'] = np.mean(np.sort(cost))
    data['Custo de manutenção - mediana'] = np.median(np.sort(cost))
    data['Custo de manutenção - desvio padrão'] = np.std(np.sort(cost))
    data['Custo de manutenção - variância'] = np.var(np.sort(cost))
    data['Custo - percentil95'] = np.percentile(np.sort(cost), 95)

    with open('../../assets/data/ex2.json', 'w') as wJson:
        json.dump(data, wJson, indent=4)
    sns.distplot(cost)
    plt.savefig("../../assets/data/Ex2.png")


def main():
    vX = ex1()
    ex2(vX)


main()
