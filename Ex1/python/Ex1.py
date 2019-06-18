import numpy as np
import random as rd
from math import exp
from bokeh.plotting import output_file, show
from statistics import mean, median, mode, variance, stdev, StatisticsError
from genPlot import makeHistogram


def main():
    # Passo 1: gerar os tempos entre falhas
    rd.seed()

    # vetor X gerado
    vX = []

    for i in range(10):
        vX.append(rd.expovariate(0.001))
    vX.sort()
    print("\nvX: ", vX, "\n")

    # Passo 2: Calcular os tempos de falha
    TK = []
    for k in range(10):
        TK.append(0)
        if(k == 0):
            TK[k] = vX[k]
            TK[k] = TK[k]/87600
        else:
            for i in range(k):
                TK[k] = TK[k] + vX[i]
                TK[k] = TK[k]/87600

    print("TK: ", TK, "\n")

    # Passo 3: Calcular o valor atual dos custos de reposição
    # função  definida por lambda
    fnc = lambda x: 10*exp(-0.952380952381*x)
    CK = []
    for k in TK:
        CK.append(fnc(k))
    print("CK: ", CK, "\n")
    meanVal = mean(CK)
# Medidas de posição
    try:
        print("Média: %f\nMediana: %f\nModa: %f \n" % (meanVal,
                                                       median(CK),
                                                       mode(CK)))
    except StatisticsError:
        print("Média: %f\nMediana: %f\nSem Moda\n" % (meanVal,
                                                      median(CK)))
# Medidas de Dispersão
    print("Variância: %f\nDesvio Padrão: %f\n" % (variance(CK), stdev(CK)))
# Construção do gráfico
    # Construir histograma da distribuição exponencial

# Plot da Amostra
    plt = makeHistogram("Custo", vX, CK)
    # plt.circle(vX, CK, legend="Amostra", fill_color='red', size=8)

    output_file("plot.html")
    show(plt)
#     plt = histogram(
#        title="Tempo e custos",
#        x_axis_label="Tempo",
#        y_axis_label="Custo"
#     )
#     plt.histogram(vX, CK, legend="Flutuação")
#     plt.line(vX, meanVal, legend="Custo Médio",
#              line_color="blue", line_width=2)
#     plt.circle(vX, CK, legend="Medidas", fill_color="red", size=8)
#     show(plt)


main()
