import numpy as np
from scipy.stats import expon, poisson
from scipy import exp

# Globals
INFLATION_RATE = 0.05
ALPHA = (1.0 / (1 + INFLATION_RATE))
BETA = 10.0
LAMBDA = 0.001
TIME_INTERVAL = 87600.0
SAMPLE_SIZE = 10000000
EXPON_SCALE = (1.0 / LAMBDA)


def ex_1():

    fail_time_intervals = expon.rvs(scale=EXPON_SCALE, size=SAMPLE_SIZE)
    # print(fail_time_intervals)

    time_of_fails = np.array([fail_time_intervals[0:i + 1].sum(axis=0) / TIME_INTERVAL for i in range(SAMPLE_SIZE)])
    # print(time_of_fails)

    replacement_costs = np.array([(BETA * exp((-1.0) * ALPHA * time_of_fails[i])) for i in range(SAMPLE_SIZE)])
    # print(replacement_cost)

    mean_replacement_cost = replacement_costs.sum() / replacement_costs.shape[0]
    print("Mean Replacement Cost: %f"  % mean_replacement_cost)

    lifespawn_of_10_th_component = time_of_fails[9] - time_of_fails[8]
    print("Lifespawn of 10th component: %f" % lifespawn_of_10_th_component)

ex_1()

