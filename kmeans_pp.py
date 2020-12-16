import mykmeanssp as msp
import pandas as pd
import numpy as np
import argparse

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

#Init data frame with the input file
df = pd.read_csv(filename, header=None)
df = pd.DataFrame.to_numpy(df, dtype=np.float64)

#Init the centroids randomly by the Algorithem given
#Call using C-API to Kmeans Algorithem from HW1
#Print the initials centroids' indexes and the result of Kmeans
def k_means_pp():
    np.random.seed(0)
    centroids = np.zeros(K, dtype=int)
    centroids[0] = np.random.choice(N, 1)
    for j in range(1, K):
        probs = get_probs(centroids, j)
        centroids[j] = np.random.choice(N, 1, p=probs)
    centroids = np.ndarray.tolist(centroids)
    print(",".join([str(centroid) for centroid in centroids]))
    res = msp.calc_centroids(K, N, d, MAX_ITER, np.ndarray.tolist(df), centroids)
    for i in range(K):
        print(",".join([str(centroid) for centroid in res[i]]))

#Calc the prob for every observition by it's distance from the closest centroid
def get_probs(centroids, j):
    probs = np.zeros(N)
    index = 0
    for row in df:
        mindist = np.linalg.norm(row - df[centroids[0]]) ** 2
        for i in range(1, j):
            candidate = np.linalg.norm(row - df[centroids[i]]) ** 2
            if candidate < mindist:
                mindist = candidate
        probs[index] = mindist
        index += 1
    probs = probs / np.sum(probs)
    return probs

#The Execution of the Algorithem
k_means_pp()
