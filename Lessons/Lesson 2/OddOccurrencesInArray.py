def solution(A):
    if len(A) == 1:
        return A[0]
    X = sorted(A)
    for i in range(0, len(A) - 1, 2):
        if X[i] != X[i + 1]:
            return X[i]
    return(X[-1])
