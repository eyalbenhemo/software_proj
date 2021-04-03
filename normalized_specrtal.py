import numpy as np
import data_parser as data
import eigengap_heuristic as eh
import math


def norm_spect_clustering():
    mat = data.data
    N = data.N
    W = weighted_adjacency(N, mat)
    D = diagonal_mat_minus_sqrt(N, W)
    L = norm_laplacian(N, W, D)
    U, K = eigengap_heuristic(L)
    return matrix_T_normalize(U), K


# step 1
def weighted_adjacency(N, mat):
    W = np.zeros((N, N), dtype='float32')
    for i in range(N - 1):
        for j in range(i + 1, N):
            W[i][j] = math.exp(-0.5 * (np.linalg.norm(mat[i] - mat[j])))
    W = np.transpose(W) + W
    return W


# step 2
def diagonal_mat_minus_sqrt(N, W):
    return np.diag(np.array([math.pow(np.sum(W[i]), -0.5) for i in range(N)]))


def norm_laplacian(N, W, D):
    return np.identity(N, dtype='float32') - D @ W @ D


# step 3 and 4
def eigengap_heuristic(L):
    Abar, Qbar = eh.QR_iter(L)
    K = eh.set_k(np.diag(Abar))
    ind = np.argsort(np.diag(Abar))[0:K]
    U = Qbar[:, ind]
    return U, K


# step 5
def matrix_T_normalize(U):
    normalization_vec = np.array([np.linalg.norm(x) for x in U],
                                 dtype='float32')
    return U / normalization_vec[:, np.newaxis]
