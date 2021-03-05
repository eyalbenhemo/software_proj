#define PY_SSIZE_T_CLEAN

#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include "linalg.h"
#include <math.h>

static double ***gram_schmidt(double **A, int n) {
    int i, j;
    double ***result = malloc(2 * sizeof(double **));
    double **U = matcopy(A, n);
    double **R = zeros(n);
    double **Q = empty(n);
    for (i = 0; i < n; i++) {
        R[i][i] = normsq(U[i], n);
        Q[i] = scalarmul(Q[i], 1 / R[i][i], n);
        for (j = i + 1, j < n, j++) {
            R[i][j] = vecmul(Q[i], U[j], n);
            U[j] = vecsub(U[j], scalarmul(Q[i], R[i][j]), n);
        }
    }
    matfree(U);
    result[0] = Q;
    result[1] = R;
    return result;
}

static double ***QR_iter_exe(dobule **A, int n) {
    int i;
    double dif;
    double **tempQ;
    double ***gs;
    double ***result = malloc(2 * sizeof(double **));
    float epsilon = 0.0001;
    double **Abar = matcopy(A);
    double **Qbar = identity(n);
    for (i = 0; i < n; i++) {
        gs = gram_schmidt(Abar, n);
        Abar = matmul(gs[0], gs[1], n);
        tempQ = matmul(Qbar, gs[0], n);
        dif = matmax(matsub(matabs(Qbar), matabs(tempQ)));
        if (dif <= epsilon || dif >= -epsilon) {
            result[0] = Abar;
            result[1] = Qbar;
            return result;
        }
        Qbar = tempQ;
    }
    free(gs[0]);
    free(gs[1]);
    free(gs);
    matfree(tempQ);
    result[0] = Abar;
    result[1] = Qbar;
    return result;
}


static int set_k_exe(double **A, int n) {
    int i, k = 0;
    double candidate;
    double *eigenvalues = diag(A, n);
    for (i = 0; i < n / 2; i++) {
        candidate = fabs(eigenvalues[i] - eigenvalues[i + 1]);
        if (candidate > k) k = i;
    }
    return k;
}

static PyObject *QR_iter(PyObject *self, PyObject *args) {
    int n;
    PyObject *PyA;
    double **A;
    if (!PyArg_ParseTuple(args, "Oi", &PyA, &n)) return NULL;
}