import numpy as np

def gram_schmidt(A: np.array):
    n = len(A)
    U = np.copy(A)
    R = np.zeros((n, n))
    Q = np.empty([n, n])
    for i in range(n):
        R[i,i] = np.linalg.norm(U[i])**2
        Q[i] = U[i] / R[i,i]
        for j in range(i + 1, n):
            R[i,j] = np.transpose(Q[i]) @ U[j]
            U[j] = U[j] - Q[i]*R[i,j]
    return {"Q" : Q, "R": R}



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
        if dif <= epsilon and dif >= -epsilon:
            return {"Abar" : Abar, "Qbar" : Qbar}
        Qbar = tempQ
    return {"Abar": Abar, "Qbar": Qbar}



def set_k(A: np.array):
    k = 0
    n = len(A)
    eigenvalues = np.diag(A)
    for i in range(n//2):
        candidate = abs(eigenvalues[i] - eigenvalues[i+1])
        if candidate > k:
            k = candidate
    return int(round(k))



