import data_parser as data
from normalized_specrtal import norm_spect_clustering
from kmeans_pp import k_means_pp as kmeans


def print_results(centroids, clusters, locations):
    print("centroids init locations")
    print(",".join([str(centroid) for centroid in centroids]))
    print("------------------------")
    print("centroids after kmeans:")
    for i in range(K):
        print(",".join([str(centroid) for centroid in clusters[i]]))
    print("------------------------")
    print("observations:")
    for i in range(data.N):
        print("The " + str(i + 1) + "st obs is clustered to the " + str(locations[i] + 1) + " centroid")


# Init data and params
data.read_data()

# Informative message
print("The maximum capacity for 2-dimensional points is: N=" + str(data.max_cap[2]['N']) + " and K=" + str(
    data.max_cap[2]['K']))
print("The maximum capacity for 3-dimensional points is: N=" + str(data.max_cap[3]['N']) + " and K=" + str(
    data.max_cap[3]['K']))

# Execution of Normalized Spectral Clustering
# step 1-5
T, d_spect = norm_spect_clustering()
K = d_spect
if not data.RANDOM:
    K = data.K

# Calling the k-mean algorithm
# step 6
spec_centroids, spec_clusters, spec_locations = kmeans(T, K, data.N, d_spect, data.MAX_ITER)

# Execution of Kmeans++ HW2
kmeans_centroids, kmeans_clusters, kmeans_locations = kmeans(data.data, K, data.N, data.d, data.MAX_ITER)

# Printing
# step 7
print("------------------------")
print("---norm spect cluster---")
print("------------------------")
print_results(spec_centroids, spec_clusters, spec_locations)
print("------------------------")
print("---------Kmeans---------")
print("------------------------")
print_results(kmeans_centroids, kmeans_clusters, kmeans_locations)
print("------------------------")
