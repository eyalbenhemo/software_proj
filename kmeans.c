#define PY_SSIZE_T_CLEAN

#include <Python.h>

/* Note: when memory error happens we return Py_None
 * according to https://moodle.tau.ac.il/mod/forum/discuss.php?d=87722 no need to free if we exit */

/* Get array of pointer to observations and calc their avg */
static double **
calc_centroids(double **observations, const int *clusterAllocations, double **new_centroids, int *clustersLengths,
               int N, int K, int d) {
    int i, j; /* Looping variables */

    for (i = 0; i < K; i++) { /* Initialize clusters lengths and values to 0 */
        clustersLengths[i] = 0;
        for (j = 0; j < d; j++) {
            new_centroids[i][j] = 0;
        }
    }

    for (i = 0; i < N; i++) { /* Add all the values of the of the observations to the relevant centroid */
        clustersLengths[clusterAllocations[i]]++; /* Update number of observations in vector */
        for (j = 0; j < d; j++) {
            new_centroids[clusterAllocations[i]][j] += observations[i][j]; /* Add observation to vector */
        }
    }

    for (i = 0; i < K; i++) { /* Update the means to all centroids */
        for (j = 0; j < d; j++) {
            if (clustersLengths[i]) {
                new_centroids[i][j] /= clustersLengths[i];
            } else {
                new_centroids[i][j] = 0;
            }
        }
    }

    return new_centroids;
}

/* Get 2 observations and calc their distance */
static double euclidian_distance(const double a[], const double b[], int d) {
    double dist = 0;
    int i = 0;
    double temp;

    for (; i < d; i++) {
        temp = (a[i] - b[i]) * (a[i] - b[i]);
        dist += temp;
    }

    return dist;
}

/* Get pointer to observation and pointer to array of centroid and return the index of closest centroid */
static int find_closest_centroid(const double a[], double **centroids, int K, int d) {
    double min_dist = -1;
    int min_cent = 0;
    int k = 0;
    double distance;
    for (; k < K; k++) {
        distance = euclidian_distance(a, centroids[k], d);
        if (distance < min_dist || min_dist == -1) {
            min_dist = distance;
            min_cent = k;
        }
    }
    return min_cent;
}

/* Get 2 array of centroids and check if they equal */
static int check_if_equals(double **new_centroids, double **centroids, int K, int d) {
    int i, j;

    for (i = 0; i < K; i++) {
        for (j = 0; j < d; j++) {
            if (centroids[i][j] != new_centroids[i][j]) {
                return 0;
            }
        }
    }

    return 1;
}

/* Get centroids, MAX_ITER and observations
 * Calc centroids while num of iter <= MAX_ITER and last(centroids) != centroids
 * return centroids */
static double **
approximation_loop(double **observations, double **centroids, int **clusterAllocations_pointer, int N, int K, int d,
                   int MAX_ITER) {
    int i, j;
    double **newCentroids; /* New centroids to be returned */
    int *clusterAllocations = *clusterAllocations_pointer;
    int *clustersLengths; /* Create array of how many observations go to each centroid */
    double **temp; /* Swap variable */
    newCentroids = malloc(K * sizeof(double *));
    if (newCentroids == NULL) {
        return NULL;
    }
    clustersLengths = calloc(K, sizeof(int));
    if (clustersLengths == NULL) {
        return NULL;
    }

    for (i = 0; i < K; i++) { /* Initialize clusters lengths and values to 0 */
        newCentroids[i] = calloc(d, sizeof(double));
        if (newCentroids[i] == NULL) {
            return NULL;
        }
    }
    for (j = 0; j < MAX_ITER; j++) {
        for (i = 0; i < N; i++) {
            clusterAllocations[i] = find_closest_centroid(observations[i], centroids, K, d);
        }
        calc_centroids(observations, clusterAllocations, newCentroids, clustersLengths, N, K, d);
        if (check_if_equals(centroids, newCentroids, K, d)) {
            break;
        }
        if (!j) {
            centroids = newCentroids;
            newCentroids = malloc(K * sizeof(double *));
            if (newCentroids == NULL) {
                return NULL;
            }
            for (i = 0; i < K; i++) {
                newCentroids[i] = calloc(d, sizeof(double));
                if (newCentroids[i] == NULL) {
                    return NULL;
                }
            }
        } else {
            temp = centroids;
            centroids = newCentroids;
            newCentroids = temp;
        }
    }
    if (newCentroids != centroids) {
        for (i = 0; i < K; i++) {
            free(newCentroids[i]);
        }
        free(newCentroids);
    }
    free(clustersLengths);
    return centroids;
}

/* C-API function: Parse the arguments from python,
 * Call the C function to execute Kmeans Algorithem */
static PyObject *calc_centroids_capi(PyObject *self, PyObject *args) {
    int K, N, d, MAX_ITER, i, j;
    double **observations, **centroids, **result;
    int *clusterAllocations;
    PyObject *Pyobservations, *K_initial_index, *PyCentroids, *Pysublists, *PyLocations, *item;
    /* Take care for the format of how get params to be like excepted */
    if (!PyArg_ParseTuple(args, "iiiiOO", &K, &N, &d, &MAX_ITER, &Pyobservations, &K_initial_index)) {
        return NULL;
    }

    observations = malloc(N * sizeof(double *));
    if (observations == NULL) {
        Py_RETURN_NONE;
    }
    centroids = malloc(K * sizeof(double *));
    if (centroids == NULL) {
        Py_RETURN_NONE;
    }
    clusterAllocations = malloc(N * sizeof(int));
    if (clusterAllocations == NULL) {
        Py_RETURN_NONE;
    }
    for (i = 0; i < N; i++) { /* Taking the observations from Python to C list */
        observations[i] = malloc(d * sizeof(double));
        if (observations[i] == NULL) {
            Py_RETURN_NONE;
        }
        item = PyList_GetItem(Pyobservations, i);
        for (j = 0; j < d; j++) {
            observations[i][j] = PyFloat_AsDouble(PyList_GetItem(item, j));
        }
    }
    for (i = 0; i < K; i++) { /* Initializing the first K centroid based on the Python Centroids */
        centroids[i] = observations[PyLong_AsLong(PyList_GetItem(K_initial_index, i))];
    }
    /* Call approximation_loop and return the centroids */
    result = approximation_loop(observations, centroids, &clusterAllocations, N, K, d, MAX_ITER);
    if (result == NULL) {
        Py_RETURN_NONE;
    }

    /* Create python list of locations */
    PyLocations = PyList_New(0);
    for (i = 0; i < N; i++) {
        PyList_Append(PyLocations, PyLong_FromLong(clusterAllocations[i]));
    }

    /* Free allocation in C */
    free(clusterAllocations);
    for (i = 0; i < N; i++) {
        free(observations[i]);
    }
    free(observations);
    free(centroids);
    for (i = 0; i < K; i++) {
        free(result[i]);
    }
    free(result);

    return Py_BuildValue("O", PyLocations);
}

/* The C-API function that will be available to the API */
static PyMethodDef capiMethods[] = {
        {"calc_centroids",                   /* the Python method name that will be used */
                (PyCFunction) calc_centroids_capi, /* the C-function that implements the Python function and returns static PyObject*  */
                      METH_VARARGS,           /* flags indicating parametersaccepted for this function */
                         PyDoc_STR(
                                 "Kmeans Algorithem get the params and the k_initials and calc the centroids")}, /* The docstring for the function */
        {NULL,  NULL, 0, NULL}
};

/* The C-API module */
static struct PyModuleDef moduledef = {
        PyModuleDef_HEAD_INIT,
        "mykmeanssp", /* name of module */
        NULL, /* Kmeans Algorithem */
        -1,  /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
        capiMethods /* the PyMethodDef array from before containing the methods of the extension */
};

PyMODINIT_FUNC
PyInit_mykmeanssp(void) {
    PyObject *m;
    m = PyModule_Create(&moduledef);
    if (!m) {
        return NULL;
    }
    return m;
}
