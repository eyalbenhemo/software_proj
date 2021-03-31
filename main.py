import data_parser as data
from normalized_specrtal import norm_spect_clustering
from kmeans_pp import k_means_pp as kmeans
import pandas as pd
from create_visualization import create_visualization_file
import time

start = time.time()


def write_clusters(locations, f, K):
    clusters = pd.DataFrame(locations).groupby([0]).indices
    for i in range(K):
        f.write('\n')
        f.write(','.join(map(str, clusters[i])))


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
spec_locations = kmeans(T, K, data.N, d_spect, data.MAX_ITER)
# Execution of Kmeans++ HW2
kmeans_locations = kmeans(data.data, K, data.N, data.d, data.MAX_ITER)

# Generate clusters.txt
f = open("clusters.txt", 'w')
f.write(str(K))
write_clusters(spec_locations, f, K)
write_clusters(kmeans_locations, f, K)
f.close()

# Generate clusters.pdf
create_visualization_file(data, spec_locations, kmeans_locations)
print(str((time.time() - start) / 60))
