from random import sample, random, seed
from math import exp
from statistics import mean, median, mode, stdev, variance, StatisticsError


def fx(x):
    return 0.001*exp(-0.001*x)


# gerar vetor de tamanho 20
def main():
    seed(random())
    vectorT = sample(range(0, 87600), 20)
    vectorT.sort()
# vetor de tempo t
    print(vectorT)
# vetor das diferenças da Variável X
    vectorX = []
    for i in range(1, len(vectorT)):
        vectorX.append(vectorT[i]-vectorT[i-1])

# Intervalos entre falhas
    print("X\n")
    print(vectorX)
    print()

# Para cada medida X, efetuar a medida de densidade de probabilidade
    xDensity = []
    for i in vectorX:
        xDensity.append(fx(i))

    print("xDensity\n")
    print(xDensity)
    print()

# Medidas de posição
    try:
        print("Média: %f\nMediana: %f\nModa: %f \n" % (mean(xDensity),
                                                        median(xDensity),
                                                        mode(xDensity)))
    except StatisticsError:
        print("Média: %f\nMediana: %f\nSem Moda\n" % (mean(xDensity),
                                                       median(xDensity)))
# Medidas de Dispersão
    print("Variância: %f\nDesvio Padrão: %f\n" % (variance(xDensity),
                                                    stdev(xDensity)))


main()
# lambda expression p/ a função f
