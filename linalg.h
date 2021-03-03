//
// Created by shazi on 3/3/2021.
//

#ifndef KMEANS_LINALG_H
#define KMEANS_LINALG_H

double** transpose(double** A, int rows, int cols);
double** matmul(double** A, double** B, int n);
double vecmul(double* A, double* B, int n);
double* scalarmul(double* A, double scalar, int n);
double** matsub(double** A, double** B, int n);
double** matcopy(double** A, int n);
double matmax(double** A, int n);
double** zeros(int n);
double** empty(int n);
void matfree(double** A, int n);
double normsq(double* v, int n);
void scalarsub(double* A, double scalar, int n);
double* vecsub(double* A, double* B, int n);
double** identity(int n);
double** matabs(double** A, int n);
double* diag(double** A, int n);

#endif //KMEANS_LINALG_H
