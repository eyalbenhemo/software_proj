import numpy as np
import pandas as pd
import data_parser as data
import math


def norm_spect_clustering():
    df = data.df
    N = data.N
    W = weighted_adjacency(N, df)
    np.set_printoptions(precision=1)
    # print(W)
    D = diagonal_mat_minus_sqrt(N, W)
    # print(D)
    L = norm_laplacian(N, W, D)
    print(L)


# step 1
def weighted_adjacency(N, df):
    mat = np.array([weight_foo(df[i], df[j], i, j) for i in range(N) for j in range(N)], dtype=np.float64)
    mat.shape = (N, N)
    return mat


def weight_foo(x_i, x_j, i, j):
    return 0 if i == j else math.exp(-0.5 * (np.linalg.norm(x_i - x_j) ** 2))

# step 2
def diagonal_mat_minus_sqrt(N, W):
    return np.diag(np.array([math.pow(np.sum(W[i]), -0.5) for i in range(N)]))

def norm_laplacian(N, W, D):
    return np.identity(N) - np.dot(np.dot(D, W), D)
