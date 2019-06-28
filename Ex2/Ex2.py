import numpy as np
import json
from math import exp, log


def F_x(x):
    return 1-exp(-0.001*x)


def f_x(x):
    return (-1000*log(x))


def main():
    with open("../assets/data/sort_data.json", "r") as rFile:
        data = json.load(rFile)
        Xn = data['Xn']
        rFile.close()
    Fx = []
    fx = []
    k = 0
    for i in Xn['Sample']:
        Fx.append(F_x(i))
        fx.append(f_x(Fx[k]))
        k = k+1

    print("\nFx: ", Fx, "\nfx: ", fx, "\n")
    print("percentil 95: ", np.percentile(Xn['Sample'], 95.0), "\n")


main()
