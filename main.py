import data_parser as data
from kmeans_pp import k_means_pp as kmeans
from normalized_specrtal import norm_spect_clustering

# Read the args and put them in variables
data.read_data()

# Normalized Spectral Clustering Algorithm
# steps 1-5
T = norm_spect_clustering()

# Calling the k-mean algorithm
# step 6
centroids, res = kmeans(T)

# Printing
# step 7
print(",".join([str(centroid) for centroid in centroids]))
for i in range(data.K):
    print(",".join([str(centroid) for centroid in res[i]]))
