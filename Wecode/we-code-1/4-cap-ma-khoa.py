import math

l, r = [int(num) for num in input().split()]

# use sieve of eratosthenes to find all prime numbers from 2 to sqrt(r) + 2 (in case r is a prime number)
def eratos(x):
    ans = []
    chk = []
    chk.extend([True] * (x))
    for i in range(2, x):
        if chk[i] == True:
            for j in range(2, x // i):
                chk[i * j] = False
            ans.append(i)
    return ans


# defactoring n into prime factors from a list of prime numbers (to utilize)
def primeFactors(n, primes):
    factors = []
    # Divide by primes until n is 1 or prime is greater than sqrt(n)
    for prime in primes:
        if prime * prime > n:
            break
        while n % prime == 0:
            factors.append(prime)
            n //= prime

    # If n is a prime greater than sqrt(n)
    if n > 1:
        factors.append(n)

    return factors


a = []
primeList = eratos(int(math.sqrt(r)) + 2)

for i in range(l, r + 1):
    temp = primeFactors(i, primeList)
    temps = set(temp)
    if len(temp) == len(temps):
        a.append(temps)
cnt = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if len(a[i].intersection(a[j])) == 0:
            #check if prime factors of a[i] and a[j] have no common elements
            #=> a[i]*a[j] is a valid pair
            cnt += 1
print(cnt)
