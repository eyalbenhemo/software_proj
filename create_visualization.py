import numpy as np
from matplotlib import pyplot as plt

def jaccard(blobs, locations):
    n = len(blobs)
    locations = np.array(locations)
    mat_locs = np.fromfunction(lambda i, j: locations[i] == locations[j], (n, n), dtype = int)
    mat_blobs = np.fromfunction(lambda i, j: blobs[i] == blobs[j], (n,n), dtype = int)
    numerator_mat = mat_blobs & mat_locs
    denominator_mat = mat_blobs | mat_locs
    numerator = np.sum(numerator_mat) - n
    denominator = np.sum(denominator_mat) - n
    if(denominator == 0):
        return 0
    return numerator / denominator



def generate_info(data, spec_jaccard, kmeans_jaccard):
    res = "Data was generated from the following values:\n" \
          "n = {} , k = {}\n" \
          "The k that was used for both algorithms was {}\n" \
          "The Jaccard measure for Spectral Clustering: {}\n" \
          "The Jaccard measure for K-means: {}".format(data.N, data.orijK, data.K, spec_jaccard, kmeans_jaccard)
    return res


def create_2d(data, spec_locations, kmeans_locations):
    fig, (spectral, kmeans) = plt.subplots(1, 2)
    cmap = plt.cm.jet
    x = data.data[:,0]
    y = data.data[:,1]
    spectral.set_title('Normalized spectral clustering')
    kmeans.set_title('K-means++')
    spectral.scatter(x,y, c = spec_locations, cmap=cmap)
    kmeans.scatter(x,y, c = kmeans_locations, cmap=cmap)
    spec_jaccard = jaccard(data.blobs, spec_locations)
    kmeans_jaccard = jaccard(data.blobs, kmeans_locations)
    info = generate_info(data, spec_jaccard, kmeans_jaccard)
    fig.subplots_adjust(bottom = 0.3)
    plt.figtext(x = 0.5, y = 0.01, s = info, ha="center", fontsize=12)
    #plt.show()
    fig.savefig("clusters.pdf")


def create_3d(data, spec_locations, kmeans_locations):
    fig, (spectral, kmeans) = plt.subplots(1, 2, subplot_kw=dict(projection='3d'))
    cmap = plt.cm.jet
    x = data.data[:, 0]
    y = data.data[:, 1]
    z = data.data[:, 2]
    spectral.set_title('Normalized spectral clustering')
    kmeans.set_title('K-means++')
    spectral.scatter(x, y, z, c=spec_locations, cmap=cmap)
    kmeans.scatter(x, y, z, c=kmeans_locations, cmap=cmap)
    spec_jaccard = jaccard(data.blobs, spec_locations)
    kmeans_jaccard = jaccard(data.blobs, kmeans_locations)
    info = generate_info(data, spec_jaccard, kmeans_jaccard)
    fig.subplots_adjust(bottom=0.2)
    plt.figtext(x = 0.5, y = 0.01, s = info, ha="center", fontsize=12)
    #plt.show()
    fig.savefig("clusters.pdf")


def create_visualization_file(data, spec_locations, kmeans_locations):
    if len(data.data[0]) == 2:
        create_2d(data, spec_locations, kmeans_locations)
    else:
        create_3d(data, spec_locations, kmeans_locations)