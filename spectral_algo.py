import data_parser as data
from kmeans_pp import k_means_pp as kmeans
from normalized_specrtal import norm_spect_clustering

# The Normalized Spectral Clustering Algorithm
def spectral_algo():
    # Normalized Spectral Clustering Algorithm
    # steps 1-5
    T, K = norm_spect_clustering()

    # Calling the k-mean algorithm
    # step 6
    centroids, centroids_new, locations = kmeans(T, K, data.N, K, data.MAX_ITER)

    # Printing
    # step 7
    print("K=" + str(K))
    print("------------------------")
    print("centroids init locations")
    print(",".join([str(centroid) for centroid in centroids]))
    print("------------------------")
    print("centroids after kmeans:")
    for i in range(K):
        print(",".join([str(centroid) for centroid in centroids_new[i]]))
    print("------------------------")
    print("observations:")
    for i in range(data.N):
        print("The " + str(i + 1) + " obs is")
        print([str(obs) for obs in data.data[i]])
        print("This obs clustered to the " + str(locations[i] + 1) + " centroid")
    print("------------------------")




