import mykmeanssp as msp
import pandas as pd
import numpy as np
import argparse
from datetime import datetime

# Read the args and put them in variables
parser = argparse.ArgumentParser()
parser.add_argument("K", type=int)
parser.add_argument("N", type=int)
parser.add_argument("d", type=int)
parser.add_argument("MAX_ITER", type=int)
parser.add_argument("filename", type=str)
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

# Init data frame with the input file
df = pd.read_csv(filename, header=None)
df = pd.DataFrame.to_numpy(df, dtype=np.float64)


# Init the centroids randomly by the Algorithem given
# Call using C-API to Kmeans Algorithem from HW1
# Print the initials centroids' indexes and the result of Kmeans
def k_means_pp():
    np.random.seed(0)
    centroids = np.zeros(K, dtype=int)
    centroids[0] = np.random.choice(N, 1)
    centroidvalues = np.empty([K,d])
    centroidvalues[0] = df[centroids[0]].copy()
    print(datetime.now())
    min = np.full(N, fill_value=float('inf'))
    for j in range(1, K):
        p = get_probs(centroidvalues, j, min)
        centroids[j] = np.random.choice(N, 1, p=p[0])
        centroidvalues[j] = df[centroids[j]].copy()
        min = p[1]
    print(datetime.now())
    centroids = np.ndarray.tolist(centroids)
    print(",".join([str(centroid) for centroid in centroids]))
    res = msp.calc_centroids(K, N, d, MAX_ITER, np.ndarray.tolist(df), centroids)
    for i in range(K):
        temp = ["{:.16f}".format(np.float64(c)) for c in res[i]]
        print(*temp, sep=",")


# Calc the prob for every observition by it's distance from the closest centroid
def get_probs(centroidvalues, j, min):
    distances = df - centroidvalues[j-1]
    distances = np.linalg.norm(distances, axis = 1) ** 2
    mintemp = np.minimum(distances, min)
    return mintemp / np.sum(mintemp), mintemp
# The Execution of the Algorithm
k_means_pp()
print(datetime.now())