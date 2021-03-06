import numpy as np


def gram_schmidt(A: np.array):
    n = len(A)
    U = np.copy(A)
    R = np.zeros((n, n))
    Q = np.empty([n, n])
    for i in range(n):
        R[i, i] = np.linalg.norm(U[i])
        Q[i] = U[i] / R[i, i]
        for j in range(i + 1, n):
            R[i, j] = np.transpose(Q[i]) @ U[j]
            U[j] = U[j] - R[i, j] * Q[i]
    return {"Q": Q, "R": R}


def QR_iter(A: np.array):
    n = len(A)
    epsilon = 0.0001
    Abar = np.copy(A)
    Qbar = np.identity(n)
    for i in range(n):
        gs = gram_schmidt(Abar)
        Abar = gs["Q"] @ gs["R"]
        tempQ = Qbar @ gs["Q"]
        dif = np.max(np.abs(Qbar) - np.abs(tempQ))
        if -epsilon <= dif <= epsilon:
            break
        Qbar = tempQ
    return {"Abar": Abar, "Qbar": Qbar}


def set_k(eigenvalues: np.array):
    k = 0
    lambda_k = 0
    n = len(eigenvalues)
    for i in range(n // 2):
        candidate = abs(eigenvalues[i] - eigenvalues[i + 1])
        if candidate > lambda_k:
            k = i
            lambda_k = candidate
    return k+1
