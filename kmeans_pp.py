import mykmeanssp as msp
import numpy as np
import data_parser as data


# Call using C-API to Kmeans Algorithm from HW1
# Print the initials centroids' indexes and the result of Kmeans
def k_means_pp(mat, K):
    np.random.seed(0)
    centroids = np.zeros(K, dtype=int)
    centroids[0] = np.random.choice(data.N, 1)
    centroidvalues = np.empty([K, K])
    centroidvalues[0] = mat[centroids[0]].copy()
    min = np.full(data.N, fill_value=float('inf'))
    for j in range(1, K):
        p = get_probs(mat, centroidvalues, j, min)
        centroids[j] = np.random.choice(data.N, 1, p=p[0])
        centroidvalues[j] = mat[centroids[j]].copy()
        min = p[1]
    centroids = np.ndarray.tolist(centroids)
    res = msp.calc_centroids(K, data.N, K, data.MAX_ITER, np.ndarray.tolist(mat), centroids)
    return centroids, res


# Calc the prob for every observition by it's distance from the closest centroid
def get_probs(mat, centroidvalues, j, min):
    distances = mat - centroidvalues[j - 1]
    distances = np.linalg.norm(distances, axis=1) ** 2
    mintemp = np.minimum(distances, min)
    return mintemp / np.sum(mintemp), mintemp
