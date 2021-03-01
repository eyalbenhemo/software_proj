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
    parser.add_argument("K", type=int)
    parser.add_argument("N", type=int)
    parser.add_argument("d", type=int)
    parser.add_argument("filename", type=str)
    args, unknown_args = parser.parse_known_args()
    K = args.K
    N = args.N
    d = args.d
    filename = args.filename

    # Assertions
    assert len(unknown_args) == 0, "4 arguments needed"
    assert (K is not None and N is not None and d is not None and filename is not None), "4 arguments needed"
    assert K > 0 and N > 0 and d > 0, "K, N, d Have to be positive"
    assert K < N, "K must be less than N"
    # Init data frame with the input file
    df = pd.DataFrame.to_numpy(pd.read_csv(filename, header=None), dtype=np.float64)