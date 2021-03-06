import data_parser as data
from spectral_algo import spectral_algo

# Init data and params
data.read_data()

# Informative message
print("The maximum capacity for 2-dimensional points is: N="+str(data.N2)+" and K="+str(data.K2))
print("The maximum capacity for 3-dimensional points is: N="+str(data.N3)+" and K="+str(data.K3))

# Execution of Normalized Spectral Clustering
spectral_algo()

