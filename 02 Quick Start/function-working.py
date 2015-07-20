__author__ = 'adelli'


def isPrime(n=1):
    if n == 1:
        # print('1 is a prime number')
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False

        else:
            # print('{} is a Prime number'.format(n))
            return True

def primes(n=1):
    while(True):
        if isPrime(n) : yield n
        n +=1

for n in primes():
    if n > 100 : break
    print(n)

