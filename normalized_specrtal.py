import numpy as np
import data_parser as data
import eigengap_heuristic as eh


# Calling all the steps in the algorithm
def norm_spect_clustering(start):
    mat = data.data
    N = data.N
    W = weighted_adjacency(N, mat)
    D = diagonal_mat_minus_sqrt(W)
    L = norm_laplacian(N, W, D)
    U = eigengap_heuristic(L, start)
    return matrix_T_normalize(U)


# step 1
def weighted_adjacency(N, mat):
    W = np.array([np.exp(-0.5 * (np.linalg.norm(mat[i] - mat, axis=1))) for i in
                  range(N)])
    np.fill_diagonal(W, 0)
    return W


# step 2
def diagonal_mat_minus_sqrt(W):
    return np.linalg.inv(np.sqrt(np.diag(np.sum(W, axis=1))))


def norm_laplacian(N, W, D):
    return np.identity(N, dtype='float32') - D @ W @ D


# step 3 and 4
def eigengap_heuristic(L, start):
    Abar, Qbar = eh.QR_iter(L)
    data.K = eh.set_k(np.diag(Abar)) if data.RANDOM else data.orijK
    ind = np.argsort(np.diag(Abar))[0:data.K]
    U = Qbar[:, ind]
    return U


# step 5
def matrix_T_normalize(U):
    normalization_vec = np.array([np.linalg.norm(x) for x in U],
                                 dtype='float32')
    return U / normalization_vec[:, np.newaxis]
