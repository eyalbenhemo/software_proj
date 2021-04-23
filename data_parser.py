import argparse
import pandas as pd
from numpy.random import randint as random
from sklearn.datasets import make_blobs

max_cap = {2: {'N': 460, 'K': 20},
           3: {'N': 460, 'K': 20}}

K = None
N = None
d = None
MAX_ITER = 300
data = None
RANDOM = True
blobs = None
orijK = None


# Read the args, save global variables and generate the data
def read_data():
    print("The maximum capacity for 2-dimensional points is: N=" +
          str(max_cap[2]['N']) + " and K=" + str(max_cap[2]['K']))
    print("The maximum capacity for 3-dimensional points is: N=" +
          str(max_cap[3]['N']) + " and K=" + str(max_cap[3]['K']))

    global K, N, d, MAX_ITER, data, RANDOM, blobs, orijK
    d = random(low=2, high=4)
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
