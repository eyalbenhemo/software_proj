import data_parser as data
from spectral_algo import spectral_algo

N2, K2, N3, K3 = 1, 1, 1, 1

# Informative message
# print("The maximum capacity for 2-dimensional points is: N="+str(N2)+" and K="+str(K2))
# print("The maximum capacity for 3-dimensional points is: N="+str(N3)+" and K="+str(K3))

# Init data and params
data.read_data()


# Execution of Normalized Spectral Clustering
spectral_algo()

