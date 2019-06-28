# import block
import random as rd
import json
# method block
from math import exp
from bokeh.io import export_png
from statistics import mean, median, mode, variance, stdev, StatisticsError
from genPlot import makeHistogram


def main():
    # Passo 1: gerar os tempos entre falhas
    rd.seed()
    # json data
    data = {}
    # vetor X gerado
    vX = []

    for i in range(1000000):
        vX.append(int(rd.expovariate(0.001)))
    vX.sort()

    # Passo 2: Calcular os tempos de falha
    TK = []
    for k in range(len(vX)):
        TK.append(0)
        if(k == 0):
            TK[k] = vX[k]
        else:
            for i in range(k):
                TK[k] = TK[k] + vX[i]
        TK[k] = TK[k] / 87600


    # Passo 3: Calcular o valor atual dos custos de reposição
    # função  definida por lambda
    # 0.952380952381 obtido de: 1/(1+r), com r = 0.05
    fnc = lambda x: 10*exp(-0.952380952381*x)
    CK = []
    for k in TK:
        CK.append(fnc(k))
    meanVal = mean(CK)
    # gen Json file for next exercises
# Medidas de posição
    try:
        print("Média: %f\nMediana: %f\nModa: %f \n" % (meanVal,
                                                       median(CK),
                                                       mode(CK)))

        data['X'] = vX
        data['Tk'] = TK
        data['cost'] = CK
        data['mean'] = meanVal
        data['variance'] = variance(CK)
        data['mode'] = mode(CK)
        data['stdev'] = stdev(CK)
    except StatisticsError:
        print("Média: %f\nMediana: %f\nSem Moda\n" % (meanVal,
                                                      median(CK)))
        data['X'] = vX
        data['Tk'] = TK
        data['cost'] = CK
        data['mean'] = meanVal
        data['variance'] = variance(CK)
        data['mode'] = 0
        data['stdev'] = stdev(CK)
# Medidas de Dispersão
    print("Variância: %f\nDesvio Padrão: %f\n" % (variance(CK), stdev(CK)))
# Construção do gráfico
    with open("../../assets/data/generated.json", "w") as wFile:
        json.dump(data, wFile, indent=4)
        wFile.close()
    # Construir histograma da distribuição exponencial

# Plot da Amostra
    plt = makeHistogram("Relação de custo e tempo entre falhas", vX, CK)
    # plt.circle(vX, CK, legend="Amostra", fill_color='red', size=8)

    export_png(plt, filename="../../assets/data/genPlot.png")


main()
