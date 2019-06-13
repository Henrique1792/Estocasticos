import random as rd


def main():
    # Passo 1: gerar os tempos entre falhas
    # fixando seed
    rd.seed()

    # vetor X gerado
    vX = []

    for i in range(10):
        vX.append(rd.expovariate(0.001))
    vX.sort()
    print(vX)

    # Passo 2: Calcular os tempos de falha
    TK = []
    for k in range(10):
        TK.append(0)
        for i in range(k):
            TK[k] = TK[k] + vX[i]

    print(TK)

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
