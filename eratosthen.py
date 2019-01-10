'''
def sieve(n):
    not_prime = []
    for i in range(2, n+1):
        if i not in not_prime:
            print(i)
            for j in range(i*i, n+1, i):
                not_prime.append(j)
sieve(10000)


kotata/pumata

'''


primes = []

for i in range(2,10000):
    primes.append(i)


#removing nonprimes
for i in primes:
    if i % 2 == 0 and i != 2:
        primes.remove(i)


for i in primes:
    if i % 3 == 0 and i !=3:
        primes.remove(i)

for i in primes:
    if i % 5 == 0 and i !=5:
        primes.remove(i)

for i in primes:
    if i % 7 == 0 and i !=7:
        primes.remove(i)

print(primes)
'''
?????????????????

    if i == 1:
        primes.remove(i)
    if i % 2 == 0:
        primes.remove(i)

print(primes)
for i in primes:
    if i % 3 == 0:
        primes.remove(i)

for i in primes:
    if i % 5 == 0:
        primes.remove(i)

for i in primes:
    if i % 7 == 0:
        primes.remove(i)

print(primes)
'''
