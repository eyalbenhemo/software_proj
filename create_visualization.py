import numpy as np
from matplotlib import pyplot as plt


def jaccard(blobs, locations):
    n = len(blobs)
    mat_locs = np.fromfunction(lambda i, j: locations[i] == locations[j],
                               (n, n), dtype=int)
    mat_blobs = np.fromfunction(lambda i, j: blobs[i] == blobs[j], (n, n),
                                dtype=int)
    numerator_mat = mat_blobs & mat_locs
    denominator_mat = mat_blobs | mat_locs
    numerator = np.sum(numerator_mat) - n
    denominator = np.sum(denominator_mat) - n
    return 0 if denominator == 0 else numerator / denominator


def generate_info(data, spec_jaccard, kmeans_jaccard):
    res = "Data was generated from the values:\n" \
          "n = {} , k = {}\n" \
          "The k that was used for both algorithms was {}\n" \
          "The Jaccard measure for Spectral Clustering: {}\n" \
          "The Jaccard measure for K-means: {}" \
        .format(data.N, data.orijK, data.K, spec_jaccard, kmeans_jaccard)
    return res


def create_visualization_file(data, spec_locations, kmeans_locations, dim):
    if dim == 3:
        fig, (spectral, kmeans) = plt.subplots(1, 2, figsize=(7, 5.5),
                                               subplot_kw=dict(projection='3d'))
    else:
        fig, (spectral, kmeans) = plt.subplots(1, 2, figsize=(7, 5.5))
    cmap = plt.cm.jet
    x = data.data[:, 0]
    y = data.data[:, 1]
    z = (data.data[:, 2] if dim == 3 else None)
    spectral.set_title('Normalized spectral clustering')
    kmeans.set_title('K-means')
    spectral.scatter(x, y, z, c=spec_locations, cmap=cmap)
    kmeans.scatter(x, y, z, c=kmeans_locations, cmap=cmap)
    spec_jaccard = jaccard(data.blobs, spec_locations)
    kmeans_jaccard = jaccard(data.blobs, kmeans_locations)
    info = generate_info(data, spec_jaccard, kmeans_jaccard)
    fig.subplots_adjust(bottom=0.3)
    plt.figtext(x=0.5, y=0.05, s=info, ha="center", fontsize=12)
    fig.savefig("clusters.pdf")
