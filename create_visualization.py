from matplotlib import pyplot as plt


def generate_info(data):
    res = "Data was generated from the following values:\n" \
          "n = {} , k = {}\n" \
          "The k that was used for both algorithms was {}\n" \
          "The Jaccard measure for Spectral Clustering: {}\n" \
          "The Jaccard measure for K-means: {}".format("n", "k", "a", "b", "c")
    return res


def create_2d(data, spec_locations, kmeans_locations):
    fig, (spectral, kmeans) = plt.subplots(1, 2)
    cmap = plt.cm.jet
    x = data.data[:, 0]
    y = data.data[:, 1]
    spectral.set_title('Normalized spectral clustering')
    kmeans.set_title('K-means++')
    spectral.scatter(x, y, c=spec_locations, cmap=cmap)
    kmeans.scatter(x, y, c=kmeans_locations, cmap=cmap)
    info = generate_info(data)
    plt.figtext(0.5, 0.01, info, ha="center", fontsize=18,
                bbox={"alpha": 0.5, "pad": 5})
    plt.show()


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
    info = generate_info(data)
    plt.figtext(0.5, 0.01, info, ha="center", fontsize=18,
                bbox={"alpha": 0.5, "pad": 5})
    plt.show()


def create_visualization_file(data, spec_locations, kmeans_locations):
    if len(data.data[0]) == 2:
        create_2d(data, spec_locations, kmeans_locations)
    else:
        create_3d(data, spec_locations, kmeans_locations)
