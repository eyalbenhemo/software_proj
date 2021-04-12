import numpy as np
import data_parser as data

epsilon = 0.0001


# Thr modified gram schmidt algorithm
def gram_schmidt(A, n):
    U = np.copy(A)
    R = np.zeros((n, n), dtype='float32')
    Q = np.empty([n, n], dtype='float32')
    for i in range(n):
        R[i, i] = np.linalg.norm(U[:, i])
        if R[i, i] == 0:
            # https://moodle.tau.ac.il/mod/forum/discuss.php?d=77599 This is
            # really rear, thus we decided to exit with an appropriate error
            # message
            exit("R[" + str(i) + ", " + str(i) + "]== 0. Please try again.")
        Q[:, i] = U[:, i] / R[i, i]

        # The code below is the inner loop in the algorithm, written with np
        # methods instead of loops

        # The j'th element in the i'th row in R from i'th element till the
        # end equal to the i'th column in Q multiple the j'th column in U
        R[i, i + 1:] = np.transpose(Q[:, i]) @ U[:, i + 1:]
        # Take the i'th column in Q and mul it with each scalar in the i'th
        # row from the (i+1)'th element till the end. Subtract each vector we
        # got from the matching column in U.
        U[:, i + 1:] -= R[i, i + 1:][np.newaxis, :] * np.array(
            [Q[:, i]] * (n - i - 1)).transpose()
    return Q, R


# The QR iteration algorithm
def QR_iter(A):
    n = data.N
    Abar = np.copy(A)
    Qbar = np.identity(n, dtype='float32')
    for i in range(n):
        Q, R = gram_schmidt(Abar, n)
        Abar = R @ Q
        tempQ = Qbar @ Q
        dif = np.max(np.abs(Qbar) - np.abs(tempQ))
        if -epsilon <= dif <= epsilon:
            break
        Qbar = tempQ
    return Abar, Qbar


# The heuristic of finding the k value
def set_k(eigenvalues):
    eigenvalues = np.sort(eigenvalues)
    k = 0
    lambda_k = 0
    for i in range(data.N // 2):
        candidate = abs(eigenvalues[i] - eigenvalues[i + 1])
        if candidate > lambda_k:
            k = i
            lambda_k = candidate
    return k + 1
