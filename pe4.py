def factorize(n):
    factors = []

    i = 2
    while i <= n:
        if n % i > 0:
            i+=1
            continue
        exp = 0
        while n % i == 0:
            exp += 1
            n //= i
        factors.append((i, exp))
        if n == 1: break
        i += 1
    return factors


for i in range(1):
    n = 40
    factors = {}
    for i in range(2, n + 1):
        fcts = factorize(i)
        for f, e in fcts:
            if f in factors and e > factors[f]:
                factors[f] = e
            if f not in factors:
                factors[f] = e
    s = 1
    for f, e in factors.items():
        s *= f ** e
print(s)
