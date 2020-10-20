def check_prime(m):
    import math
    count = 1
    n = int(math.sqrt(m))
    for i in range(2, n+1):
        count += 1
        if n % i == 0:
            return False
            break
        if i == n-1:
            return True