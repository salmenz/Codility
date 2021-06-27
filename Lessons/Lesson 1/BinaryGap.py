def solution(N):
    X = bin(N)
    X = X[2:]
    r = 0
    max = 0
    for i in range(len(X)):
        if X[i] == '0':
            r += 1
        else:
            if r > max:
                max = r
            r = 0
    return max
