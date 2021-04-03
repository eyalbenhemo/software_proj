import data_parser as data
from normalized_specrtal import norm_spect_clustering
from kmeans_pp import k_means_pp as kmeans
import pandas as pd
from create_visualization import create_visualization_file
from time import time


def write_clusters(locations, f, K):
    clusters = pd.DataFrame(locations).groupby([0]).indices
    for i in range(K):
        f.write('\n')
        f.write(','.join(map(str, clusters[i])))


def generate_cluster(spec_locations, kmeans_locations):
    f = open("clusters.txt", 'w')
    f.write(str(data.K))
    write_clusters(spec_locations, f, data.K)
    write_clusters(kmeans_locations, f, data.K)
    f.close()


def main():
    start = time()
    # Init data and params
    data.read_data1()
    # Execution of Normalized Spectral Clustering. step 1-5
    T = norm_spect_clustering()
    # Calling the k-mean algorithm. step 6
    spec_locations = kmeans(T, data.K, data.N, data.K, data.MAX_ITER)
    kmeans_locations = kmeans(data.data, data.K, data.N, data.d, data.MAX_ITER)
    # Generate clusters.txt
    generate_cluster(spec_locations, kmeans_locations)
    # Generate clusters.pdf
    create_visualization_file(data, spec_locations, kmeans_locations, data.d)
    print(str(time() - start))


main()
