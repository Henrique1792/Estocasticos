import random as rd
from math import exp


def main():
    # Passo 1: gerar os tempos entre falhas
    rd.seed()

    # vetor X gerado
    vX = []

    for i in range(10):
        vX.append(rd.expovariate(0.001))
    vX.sort()
    print("vX: ", vX, "\n")

    # Passo 2: Calcular os tempos de falha
    TK = []
    for k in range(10):
        TK.append(0)
        for i in range(k):
            TK[k] = TK[k] + vX[i]

    print("TK: ", TK, "\n")

    # Passo 3: Calcular o valor atual dos custos de reposição
    # função  definida por lambda

    fnc = lambda x: 10*exp(-0.952380952381*x)
    CK = []
    for k in TK:
        CK.append(fnc(k))
    print("CK: ", CK, "\n")

# Medidas de posição
#    try:
#        print("Média: %f\nMediana: %f\nModa: %f \n" % (mean(xDensity),
#                                                        median(xDensity),
#                                                        mode(xDensity)))
#    except StatisticsError:
#        print("Média: %f\nMediana: %f\nSem Moda\n" % (mean(xDensity),
#                                                       median(xDensity)))
# Medidas de Dispersão
#    print("Variância: %f\nDesvio Padrão: %f\n" % (variance(xDensity),
    #                                                    stdev(xDensity)))


main()
