import numpy as np
import data_parser as data
import eigengap_heuristic as eh
import math


def norm_spect_clustering():
    df = data.df
    N = data.N
    # start = time.time()
    W = weighted_adjacency(N, df)
    # print(time.time() - start)
    np.set_printoptions(precision=1)
    # print(W)
    # start = time.time()
    D = diagonal_mat_minus_sqrt(N, W)
    L = norm_laplacian(N, W, D)
    print(L)
    # print("2 " + time.time() - start)
    U = eigengap_heuristic(L)
    return matrix_T_normalize(U)


# step 1
def weighted_adjacency(N, df):
    mat = np.array([weight_foo(x_i, x_j) for x_i in df for x_j in df], dtype=np.float64)
    mat.shape = (N, N)
    return mat - np.identity(N)


def weight_foo(x_i, x_j):
    return math.exp(-0.5 * (np.linalg.norm(x_i - x_j)))


# step 2
def diagonal_mat_minus_sqrt(N, W):
    return np.diag(np.array([math.pow(np.sum(W[i]), -0.5) for i in range(N)]))


def norm_laplacian(N, W, D):
    return np.identity(N) - np.dot(np.dot(D, W), D)


# step 3 and 4
def eigengap_heuristic(L):
    eigens = eh.QR_iter(L)
    k = eh.set_k(eigens["Abar"])
    ind = np.argsort(np.diag(eigens["Abar"]))[0:k]
    U = eigens["Qbar"][:, ind]
    return U




# step 5
def matrix_T_normalize(U):
    normalization_vec = np.array(np.linalg.norm(x) for x in U)
    return U / normalization_vec[:, np.newaxis]
