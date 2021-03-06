import data_parser as data
from spectral_algo import spectral_algo

# Init data and params
data.read_data()

# Informative message
print("The maximum capacity for 2-dimensional points is: N=" + str(data.max_cap[2]['N']) + " and K=" + str(
    data.max_cap[2]['K']))
print("The maximum capacity for 3-dimensional points is: N=" + str(data.max_cap[3]['N']) + " and K=" + str(
    data.max_cap[3]['K']))

# Execution of Normalized Spectral Clustering
spectral_algo()
