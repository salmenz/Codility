def solution(A):
    p1 = A[0]
    p2 = sum(A[1:])
    min = abs(p1 - p2)
    for i in range(1, len(A)-1):
        p1 += A[i]
        p2 -= A[i]
        if abs(p1 - p2) < min:
            min = abs(p1 - p2)
    return min
