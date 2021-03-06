import argparse
from numpy.random import randint as random
from sklearn.datasets import make_blobs

max_cap = {2: {'N': 20, 'K': 10},
           3: {'N': 16, 'K': 8}}

K = None
N = None
d = None
MAX_ITER = 300
data = None
RANDOM = None


def read_data():
    global K, N, d, MAX_ITER, data, RANDOM
    d = random(low=2, high=4)
    parser = argparse.ArgumentParser()
    temp, args = parser.parse_known_args()

    # Code validation
    if len(args) != 3:
        exit("3 arguments required")
    K = args[0]
    N = args[1]
    RANDOM = args[2]
    if not (K.isnumeric() and int(K) > 0):
        exit("K has to be positive number")
    if not (N.isnumeric() and int(N) > 0):
        exit("N has to be positive number")
    K = int(K)
    N = int(N)
    if K >= N:
        exit("K must be smaller than N")
    if not (RANDOM == "True" or RANDOM == "False"):
        exit("RANDOM has to be boolean")
    RANDOM = (RANDOM == "True")
    if RANDOM:
        N = random(low=max_cap[d]['N'] / 2, high=max_cap[d]['N'])
        K = random(low=max_cap[d]['K'] / 2, high=max_cap[d]['K'])
    data = make_blobs(n_samples=N, n_features=d, centers=K)[0]
