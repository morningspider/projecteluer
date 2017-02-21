from math import factorial as f
from totient import *
from numtheory import isPrime
from collections import Counter
import time
from sympy import sieve
from collections import defaultdict
from math import sqrt, factorial

def s(n):
    k = 1
    m = 1
    while m%n != 0:
        m *= k
        k += 1
    return k-1

def S(n):
    acc = 0
    for n in range(2, n+1):
        m = s(n)
        acc += m
    return acc
t = time.clock()
acc = 2
n = 1000
for p in sieve.primerange(2,n):
    e = 1
    if p == 2: e=2
    powers = []
    # first find all k for s(kp) = s(p) = p
    skip_next = False
    while (p**e) <= n:
        m = 1
        fact = 1
        while fact != 0:
            m += 1
            fact = (fact*m) % (p**e)
        #we have s(p^e) = m, now we need to find all k for which s(k*p^e) = m
        k = 1
        hits = []

        while k*(p**e) <= n and k*p**e not in powers:
            if m < 10 and k > factorial(m): break
            i, fact = 1,1
            while fact !=0:
                fact = fact*i % (k*p**e)
                i+=1
            if i-1 == m:
                hits.append(k*p**e)
                if k%p == 0:
                    powers.append(k*p**e)
            k+=1
        acc += len(list(set(hits))) * m
        if skip_next: e+=1
        e+=1

print (time.clock() - t)

acc = 0
reverse = defaultdict(list)
div = defaultdict(list)
for i in range(2, n+1):
    m = s(i)
    reverse[m].append(i)
    div[m].append(i/m)
    acc += m

bigS = 0
for i in range(2,101):

    m = 1
    acc = 1
    while acc%i != 0:
        m+=1
        acc = (m*acc)%i
    bigS += m
