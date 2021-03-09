import argparse
import pandas as pd
from numpy.random import randint as random
from sklearn.datasets import make_blobs

max_cap = {2: {'N': 200, 'K': 10},
           3: {'N': 100, 'K': 8}}

K = None
N = None
d = None
MAX_ITER = 300
data = None
RANDOM = True
blobs = None
orijK = None


def read_data():
    global K, N, d, MAX_ITER, data, RANDOM, blobs, orijK
    d = random(low=2, high=4)
    parser = argparse.ArgumentParser()
    temp, args = parser.parse_known_args()

    # Code validation
    if len(args) != 3:
        exit("3 arguments required")
    orijK = args[0]
    N = args[1]
    RANDOM = args[2]
    if not (orijK.isnumeric() and int(orijK) > 0):
        exit("K has to be positive number")
    if not (N.isnumeric() and int(N) > 0):
        exit("N has to be positive number")
    K = int(orijK)
    N = int(N)
    if K >= N:
        exit("K must be smaller than N")
    if not (RANDOM == "True" or RANDOM == "False"):
        exit("RANDOM has to be either True or False")
    RANDOM = (RANDOM != "False")
    if RANDOM:
        N = random(low=max_cap[d]['N'] / 2, high=max_cap[d]['N'])
        K = random(low=max_cap[d]['K'] / 2, high=max_cap[d]['K'])
    sample = make_blobs(n_samples=N, n_features=d, centers=K)
    data = sample[0]
    blobs = sample[1]

    # generate data.txt
    print(sample)
    data_out = pd.DataFrame(sample[0])
    data_out['new'] = sample[1]
    data_out.to_csv('data.txt', index=False, header=False)
