# import block
import random as rd
import json
import numpy as np
# method block
from math import exp
from bokeh.io import export_png
from statistics import mean, median, mode, variance, stdev, StatisticsError
from genPlot import makeHistogram
from scipy.stats import expon


def repoCost(x):
    beta = 10
    return beta*exp(-0.952380952381*x)


def main():
    data = {}
    exponScale = 0.001
    sample = 10000
    nHours = 87600
    vX = expon.rvs(scale=exponScale, size=sample)
    # print(vX)
    TK = np.array([vX[0:i+1].sum(axis=0)/nHours for i in range(sample)])
    # print(TK)
    CK = []
    for i in range(sample):
        CK.append(repoCost(TK[i]))
    
    print("10º componente: %.10f\n" % (TK[9] - TK[8]))
    print("Custo do 10º componente: %f " % CK[9])
    
    data['meanTK'] = mean(TK)
    data['varianceTK'] = variance(TK)
    data['amplitudeTK'] = max(TK) - min(TK)
    data['stdevTK'] = stdev(TK)
    data['percentileTK'] = np.percentile(TK, 95, axis=0)
    data['meanCK'] = mean(CK)

    print(data)
# Passo 2: Calcular os tempos de falha
#     TK = []
#     for k in range(len(vX)):
#         TK.append(0)
#         if(k == 0):
#             TK[k] = vX[k] / 87600
#         else:
#             for i in range(k):
#                 TK[k] = TK[k] + (vX[i] / 87600)
# 
#     # Passo 3: Calcular o valor atual dos custos de reposição
#     # função  definida por lambda
#     # 0.952380952381 obtido de: 1/(1+r), com r = 0.05
#     CK = []
#     for k in TK:
#         CK.append(repoCost(k))
#     meanVal = mean(CK)
#     # gen Json file for next exercises
# # Medidas de posição
#     try:
#         print("Média: %f\nMediana: %f\nModa: %f \n" % (meanVal,
#                                                        median(CK),
#                                                        mode(CK)))
# 
#         data['X'] = vX
#         data['Tk'] = TK
#         data['cost'] = CK
#         data['mean'] = meanVal
#         data['variance'] = variance(CK)
#         data['mode'] = mode(CK)
#         data['stdev'] = stdev(CK)
#     except StatisticsError:
#         print("Média: %f\nMediana: %f\nSem Moda\n" % (meanVal,
#                                                       median(CK)))
#         data['X'] = vX
#         data['Tk'] = TK
#         data['cost'] = CK
#         data['mean'] = meanVal
#         data['variance'] = variance(CK)
#         data['mode'] = 0
#         data['stdev'] = stdev(CK)
# # Medidas de Dispersão
#     print("Variância: %f\nDesvio Padrão: %f\n" % (variance(CK), stdev(CK)))
# # Construção do gráfico
#     with open("../../assets/data/generated.json", "w") as wFile:
#         json.dump(data, wFile, indent=4)
#         wFile.close()
#     # Construir histograma da distribuição exponencial
# 
# # Plot da Amostra
#     plt = makeHistogram("Relação de tempo de falhas e custo", TK, CK)
#     # plt.circle(vX, CK, legend="Amostra", fill_color='red', size=8)
# 
#     export_png(plt, filename="../../assets/data/genPlot.png")
# 
# 
main()
