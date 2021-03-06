import argparse
import pandas as pd
import numpy as np

K = None
N = None
d = None
MAX_ITER = 300
df = None


def read_data():
    global K, N, d, MAX_ITER, df
    parser = argparse.ArgumentParser()
    # parser.add_argument("K")
    # parser.add_argument("N")
    # parser.add_argument("d")
    # parser.add_argument("filename")
    temp, args = parser.parse_known_args()

    # Code validation
    if len(args) != 4:
        exit("4 arguments required")
    K = args[0]
    N = args[1]
    d = args[2]
    filename = args[3]
    if not (K.isnumeric() and int(K) > 0):
        exit("K has to be positive number")
    if not (N.isnumeric() and int(N) > 0):
        exit("N has to be positive number")
    if not (d.isnumeric() and int(d) > 0):
        exit("d has to be positive number")
    K = int(K)
    N = int(N)
    d = int(d)
    if K >= N:
        exit("K must be smaller than N")

    # Init data frame with the input file
    df = pd.DataFrame.to_numpy(pd.read_csv(filename, header=None), dtype=np.float64)
