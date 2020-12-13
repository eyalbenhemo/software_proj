import numpy as np
import pandas as pd
import argparse

# Read the args and put them in variables
parser = argparse.ArgumentParser()
parser.add_argument("K", nargs="?", type=int)
parser.add_argument("N", nargs="?", type=int)
parser.add_argument("d", nargs="?", type=int)
parser.add_argument("MAX_ITER", nargs="?", type=int)
parser.add_argument("filename", nargs="?", type=str)
args, unknown_args = parser.parse_known_args()
K = args.K
N = args.N
d = args.d
MAX_ITER = args.MAX_ITER
filename = args.filename

# Assertions
assert len(unknown_args) == 0, "5 arguments needed"
assert (K is not None and N is not None and d is not None and MAX_ITER is not None
        and filename is not None), "5 arguments needed"
assert K > 0 and N > 0 and d > 0 and MAX_ITER > 0, "K, N, d, MAX_ITER Have to be positive"
assert K < N, "K must be less than N"

pd.read_csv(filename)
