import argparse
import pandas as pd
from numpy.random import randint as random
from sklearn.datasets import make_blobs

max_cap = {2: {'N': 460, 'K': 10},
           3: {'N': 200, 'K': 10}}

K = None
N = None
d = None
MAX_ITER = 300
data = None
RANDOM = True
blobs = None
orijK = None


def read_data():
    print("The maximum capacity for 2-dimensional points is: N=" +
          str(max_cap[2]['N']) + " and K=" + str(max_cap[2]['K']))
    print("The maximum capacity for 3-dimensional points is: N=" +
          str(max_cap[3]['N']) + " and K=" + str(max_cap[3]['K']))

    global K, N, d, MAX_ITER, data, RANDOM, blobs, orijK
    d = random(low=2, high=4)
    d = 2
    parser = argparse.ArgumentParser()
    parser.add_argument("K")
    parser.add_argument("N")
    parser.add_argument("Random")
    args = parser.parse_args()
    orijK = args.K
    N = args.N
    RANDOM = (args.Random == "True")
    if RANDOM:
        N = random(low=max_cap[d]['N'] / 2, high=max_cap[d]['N'])
        orijK = random(low=max_cap[d]['K'] / 2, high=max_cap[d]['K'])
    else:
        if not (str(orijK).isnumeric() and int(orijK) > 0):
            exit("if no random, please send positive num for K")
        if not (str(N).isnumeric() and int(N) > 0):
            exit("if no random, please send positive num for N")
        orijK = int(orijK)
        N = int(N)
        if orijK >= N:
            exit("K must be smaller than N")
    data, blobs = make_blobs(n_samples=N, n_features=d, centers=orijK)

    # generate data.txt
    data_out = pd.DataFrame(data)
    data_out['new'] = blobs
    data_out.to_csv('data.txt', index=False, header=False)
    data = data.astype('float32')


def read_data1():
    print("The maximum capacity for 2-dimensional points is: N=" +
          str(max_cap[2]['N']) + " and K=" + str(max_cap[2]['K']))
    print("The maximum capacity for 3-dimensional points is: N=" +
          str(max_cap[3]['N']) + " and K=" + str(max_cap[3]['K']))
    import numpy as np
    global K, N, d, MAX_ITER, data, RANDOM, blobs, orijK
    parser = argparse.ArgumentParser()
    temp, args = parser.parse_known_args()

    filename = args[0]
    RANDOM = (args[2] == 'True')
    # Init data frame with the input file
    data = pd.read_csv(filename, header=None)
    data = pd.DataFrame.to_numpy(data)
    N, d = data.shape
    d -= 1
    blobs = np.array(data[:, d], dtype=int)
    data = data[:, 0:d]
    orijK = len(np.unique(blobs)) if RANDOM else int(args[1])

    # generate data.txt
    data_out = pd.DataFrame(data)
    data_out['new'] = blobs
    data_out.to_csv('data.txt', index=False, header=False)
    data = data.astype('float32')
