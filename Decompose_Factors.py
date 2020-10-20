n = 84
def decomposed(n):
    prime = [2, 3, 5, 7, 11, 13, 17, 19]
    dict = {s:0 for s in prime}
    res = ""
    for p in prime:
        while (n % p == 0):
            dict[p] += 1            
            n = n / p
            print(p, n, dict)

    for p in prime:
        print(p,"^",dict[p]) 