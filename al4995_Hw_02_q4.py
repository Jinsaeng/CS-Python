def e_approx(n):
    e = 1
    div = 1
    for i in range(1,n+1):
        div *= i
        e += 1/div
    return e
