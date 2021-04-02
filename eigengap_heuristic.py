import numpy as np


def gram_schmidt(A: np.array):
    n = len(A)
    U = np.copy(A)
    R = np.zeros((n, n))
    Q = np.empty([n, n])
    for i in range(n):
        R[i, i] = np.linalg.norm(U[:, i])
        if R[i, i] == 0:
            # https://moodle.tau.ac.il/mod/forum/discuss.php?d=77599
            # this is really rear, thus we decided to print an error message
            exit("R[" + str(i) + ", " + str(i) + "]== 0. Please try again.")
        Q[:, i] = U[:, i] / R[i, i]
        # the j'th element in the i'th row in R from i'th element till the end equal to the i'th column in Q multiple
        # the j'th column in U
        R[i, i + 1:] = Q[:, i] @ U[:, i + 1:]  # Check this row!
        # Take the i'th column in Q and mul it with each scalar in the i'th row from the (i+1)'th element till the end.
        # Subtract each vector we got from the matching column in U.
        U[:, i + 1:] -= R[i, i + 1:][np.newaxis, :] * np.transpose([Q[:, i]] * (n - i - 1))
    return {"Q": Q, "R": R}


def QR_iter(A: np.array):
    n = len(A)
    epsilon = 0.0001
    Abar = np.copy(A)
    Qbar = np.identity(n)
    for i in range(n):
        gs = gram_schmidt(Abar)
        Abar = gs["R"] @ gs["Q"]
        tempQ = Qbar @ gs["Q"]
        dif = np.max(np.abs(Qbar) - np.abs(tempQ))
        if -epsilon <= dif <= epsilon:
            break
        Qbar = tempQ
    return {"Abar": Abar, "Qbar": Qbar}


def set_k(eigenvalues: np.array):
    eigenvalues = np.sort(eigenvalues)
    k = 0
    lambda_k = 0
    n = len(eigenvalues)
    for i in range(n // 2):
        candidate = abs(eigenvalues[i] - eigenvalues[i + 1])
        if candidate > lambda_k:
            k = i
            lambda_k = candidate
    return k + 1
