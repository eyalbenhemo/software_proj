import mykmeanssp as msp
import numpy as np


# Call using C-API to Kmeans Algorithm from HW1
def k_means_pp(mat, K, N, d, MAX_ITER):
    np.random.seed(0)
    centroids = np.zeros(K, dtype=int)
    centroids[0] = np.random.choice(N, 1)
    centroids_values = np.empty([K, d])
    centroids_values[0] = mat[centroids[0]].copy()
    min_dist = np.full(N, fill_value=float('inf'))
    for j in range(1, K):
        p = get_probs(mat, centroids_values, j, min_dist)
        if np.isnan(p[0]).any():
            print("!")
        centroids[j] = np.random.choice(N, 1, p=p[0])
        centroids_values[j] = mat[centroids[j]].copy()
        min_dist = p[1]
    centroids = np.ndarray.tolist(centroids)
    centroids_new, locations = msp.calc_centroids(K, N, d, MAX_ITER, np.ndarray.tolist(mat), centroids)
    return centroids, centroids_new, locations


# Calc the prob for every observation by it's distance from the closest centroid
def get_probs(mat, centroids_values, j, min_dist):
    distances = mat - centroids_values[j - 1]
    distances = np.linalg.norm(distances, axis=1)**2
    min_temp = np.minimum(distances, min_dist)
    return min_temp / np.sum(min_temp), min_temp
