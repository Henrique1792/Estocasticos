import numpy as np

from scipy.stats import expon, poisson, norm, uniform
from scipy import exp

import matplotlib.pyplot as plt
import seaborn as sns

# Globals
INFLATION_RATE = 0.05
ALPHA = (1.0 / (1 + INFLATION_RATE))
BETA = 10.0

SAMPLE_SIZE = 100000000
TIME_PERIOD = 87600.0 / 8760.0

LAMBDA = 0.001 * 24 * 365
EXPON_SCALE = (1.0 / (0.001 * 24 * 365))


def ex_1():

    uniform_samples = uniform.rvs(size = SAMPLE_SIZE)
    # print(uniform_samples)

    exponential_samples = expon.ppf(uniform_samples, scale=EXPON_SCALE)
    # print(exponential_samples)

    fail_time_intervals = np.array([])
    while np.sum(fail_time_intervals) < TIME_PERIOD:
        fail_time_intervals = np.append(fail_time_intervals, np.random.choice(exponential_samples, 1))
        # print(np.sum(fail_time_intervals))
    # print(fail_time_intervals)

    time_of_fails = np.array([fail_time_intervals[0:i + 1].sum(axis=0) for i in range(len(fail_time_intervals))])
    # print(time_of_fails)

    lifespawn_of_components = []
    lifespawn_of_components.append(time_of_fails[0])
    lifespawn_of_components += [time_of_fails[i + 1] - time_of_fails[i] for i in range(len(time_of_fails) - 1)]
    # print(lifespawn_of_components)

    print("Lifespawn of 10th component: %f" % lifespawn_of_components[9])
    print("Lifespawn median: %f" % np.median(np.sort(lifespawn_of_components)))
    print("Lifespawn mean: %f" % np.mean(np.sort(lifespawn_of_components)))
    print("Lifespawn standard deviation: %f" % np.std(np.sort(lifespawn_of_components)))
    print("Lifespawn variance: %f" % np.var(np.sort(lifespawn_of_components)))
    print("Lifespawn 95th percentile: %f" % np.percentile(np.sort(lifespawn_of_components), 95))

    sns.set_style('darkgrid')
    sns.distplot(lifespawn_of_components)
    plt.savefig("histogram_ls.png")
    plt.clf()  

    return time_of_fails

def ex_2(times):

    replacement_costs = np.array([(BETA * exp((-1.0) * ALPHA * times[i])) for i in range(len(times))])
    # print(replacement_costs)

    print("Replacement cost of 10th component: %f" % replacement_costs[9])
    print("System's maintance cost median: %f" % np.median(np.sort(replacement_costs)))
    print("System's maintance mean: %f" % np.mean(np.sort(replacement_costs)))
    print("System's maintance standard deviation: %f" % np.std(np.sort(replacement_costs)))
    print("System's maintance variance: %f" % np.var(np.sort(replacement_costs)))
    print("System's maintance 95th percentile: %f" % np.percentile(np.sort(replacement_costs), 95))

    sns.set_style('darkgrid')
    sns.distplot(replacement_costs)
    plt.savefig("histogram_rc.png")

data = ex_1()
ex_2(data)
