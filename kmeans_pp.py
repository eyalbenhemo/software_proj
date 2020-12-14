import mykmeanssp as msp
import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("K", type=int)
parser.add_argument("N", type=int)
parser.add_argument("d", type=int)
parser.add_argument("MAX_ITER", type=int)
parser.add_argument("filename", type=str)
args = parser.parse_args()

K = args.K
N = args.N
d = args.d
MAX_ITER = args.MAX_ITER
filename = args.filename

df = pd.read_csv(filename, header=None)
df = pd.DataFrame.to_numpy(df, dtype=np.float64)


def k_means_pp(df, K, N, d, MAX_ITER):
    np.random.seed(0)
    centroids = np.zeros(K, dtype=int)
    centroids[0] = np.random.choice(N, 1)
    for j in range(1, K):
        probs = get_probs(df, centroids, j)
        centroids[j] = np.random.choice(N, 1, p=probs)

    centroids = np.ndarray.tolist(centroids)
    print(",".join([str(centroid) for centroid in centroids]))
    res = msp.calc_centroids(K, N, d, MAX_ITER, np.ndarray.tolist(df), centroids)
    for i in range(K):
        print(",".join([str(centroid) for centroid in res[i]]))


def get_probs(df, centroids, j):
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


k_means_pp(df, K, N, d, MAX_ITER)
