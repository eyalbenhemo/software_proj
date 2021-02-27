from data_parser import read_data
from kmeans_pp import k_means_pp as kmeans
from normalized_specrtal import norm_spect_clustering

# Read the args and put them in variables
read_data()

#Normalized Spectral Clustring Algorithm
norm_spect_clustering()

# Calling the k-mean algorithm
#kmeans()
