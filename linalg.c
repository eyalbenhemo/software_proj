#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double **transpose(double **A, int rows, int cols) {
    int i, j;
    double **result = malloc(cols * sizeof(double *));
    for (i = 0; i < cols; i++) {
        result[i] = malloc(rows * sizeof(double));
        for (j = 0; j < rows; j++) {
            result[i][j] = A[j][i];
        }
    }
    return result;
}

double **matmul(double **A, double **B, int n) {
    int i, j, k;
    B = transpose(B);
    double **result = malloc(n * sizeof(double *));
    for (i = 0; i < n; i++) {
        result[i] = calloc(n, sizeof(double));
        for (j = 0; j < n; j++) {
            for (k = 0; k < n; k++) {
                result[i][j] += A[i][k] * B[j][k];
            }
        }
    }
    return result;
}

double vecmul(double *A, double *B, int n) {
    int i;
    double result = 0;
    for (i = 0; i < n; i++)
        result += A[i] * B[i];
    return result;
}

double *vecsub(double *A, double *B, int n) {
    int i;
    double *result = malloc(n * sizeof(double));
    for (i = 0; i < n; i++)
        result[i] = A[i] - B[i];
    return result;
}

double *scalarmul(double *A, double scalar, int n) {
    int i;
    double *result = malloc(n * sizeof(double));
    for (i = 0; i < n; i++)
        result[i] = A[i] * scalar;
    return result;
}

void scalarsub(double *A, double scalar, int n) {
    int i;
    for (i = 0; i < n; i++) {
        A[i] -= scalar;
    }
}

double **matsub(double **A, double **B, int n) {
    int i, j;
    double **result = malloc(n * sizeof(double *));
    for (i = 0; i < n; i++) {
        result[i] = malloc(n * sizeof(double));
        for (j = 0; j < n; j++) {
            result[i][j] = A[i][j] - B[i][j];
        }
    }
    return result;
}

double **matcopy(double **A, int n) {
    int i, j;
    double **result = malloc(n * sizeof(double *));
    for (i = 0; i < n; i++) {
        result[i] = malloc(n * sizeof(double));
        for (j = 0; i < n; i++) {
            result[i][j] = A[i][j];
        }
    }
}

double matmax(double **A, int n) {
    int i, j;
    int max = A[0][0];
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (A[i][j] > max) max = A[i][j];
        }
    }
    return max;
}

double **zeros(int n) {
    int i;
    double **result = malloc(n * sizeof(double *));
    for (i = 0; i < n; i++) result[i] = calloc(n * sizeof(double));
    return result;
}

double **empty(int n) {
    int i;
    double **result = malloc(n * sizeof(double *));
    for (i = 0; i < n; i++) result[i] = malloc(n * sizeof(double));
    return result;
}

void matfree(double **A, int n) {
    double *p = *A;
    int i;
    for (i = 0; i < n * n; i++) free(*p++);
}

double normsq(double *v, int n) {
    int i;
    int sum = 0
    for (i = 0; i < n; i++) {
        sum += v[i] * v[i];
    }
    return sum;
}

double **identity(int n) {
    int i;
    double **result = malloc(n * sizeof(dobule * ));
    for (i = 0; i < n; i++) {
        result[i] = calloc(n, sizeof(double));
        result[i][i] = 1;
    }
    return result;
}

double **matabs(double **A, int n) {
    int i, j;
    double **result = malloc(n * sizeof(dobule * ));
    for (i = 0; i < n; i++) {
        result[i] = malloc(n * sizeof(dobule));
        for (j = 0; j < n; j++) {
            result[i][j] = (A[i][j] >= 0) ? A[i][j] : -A[i][j];
        }
    }
    return result;
}

double *diag(double **A, int n) {
    int i;
    double *result = malloc(n * sizeof
    double);
    for (i = 0; i < n; i++) result[i] = A[i][i];
    return result;
}