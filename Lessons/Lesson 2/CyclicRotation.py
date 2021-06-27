def solution(A, K):
    if A == []:
        return []
    for i in range(K):
        A = [A[-1]] + A[:-1]
    return A