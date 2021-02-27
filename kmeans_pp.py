import mykmeanssp as msp
import numpy as np
import data_parser as data


# Init the centroids randomly by the algorithm given
# Call using C-API to kmeans Algorithm from HW1
# Print the initials centroids' indexes and the result of kmeans
def k_means_pp():
    np.random.seed(0)
    centroids = np.zeros(data.K, dtype=int)
    centroids[0] = np.random.choice(data.N, 1)
    for j in range(1, data.K):
        probs = get_probs(centroids, j)
        centroids[j] = np.random.choice(data.N, 1, p=probs)
    centroids = np.ndarray.tolist(centroids)
    print(",".join([str(centroid) for centroid in centroids]))
    res = msp.calc_centroids(data.K, data.N, data.d, data.MAX_ITER, np.ndarray.tolist(data.df), centroids)
    for i in range(data.K):
        print(",".join([str(centroid) for centroid in res[i]]))


# Calc the prob for every observation by it's distance from the closest centroid
# here is the bottle neck of the time complexity
def get_probs(centroids, j):
    probs = np.zeros(data.N)
    index = 0
    for row in data.df:
        mindist = np.linalg.norm(row - data.df[centroids[0]]) ** 2
        for i in range(1, j):
            candidate = np.linalg.norm(row - data.df[centroids[i]]) ** 2
            if candidate < mindist:
                mindist = candidate
        probs[index] = mindist
        index += 1
    probs = probs / np.sum(probs)
    return probs
