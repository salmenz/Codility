def solution(A):
    if not A:
        return 1
    A = sorted(A)
    for i in range(len(A)):
        if A[i] != i + 1:
            return i + 1
    return i + 2
