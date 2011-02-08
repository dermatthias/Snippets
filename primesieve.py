# Sieve of Eratosthenes

def primesieve(n) :
'''
Sieve of Eratosthenes. Finds all prime numbers up to (including) n.
'''
    max_i = (n-3) // 2
    max_p = int(n**0.5)
    sieve = [True for j in xrange(max_i + 1)]
    for p in xrange(3, max_p + 1, 2) :
        i = (p-3) // 2
        if sieve[i]:
            i2 = (p**2 - 3) // 2
            for k in xrange(i2, max_i+1, p):
                sieve[k] = False
    return [2] + [2 * j + 3 for j in xrange(len(sieve)) if sieve[j]]
