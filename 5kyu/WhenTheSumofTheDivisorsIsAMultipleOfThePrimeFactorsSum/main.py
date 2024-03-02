def sieve_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [i for i in range(n + 1) if is_prime[i]]

def ds_multof_pfs(nMin, nMax):
    primes = sieve_eratosthenes(nMax)
    results = []
    for i in range(nMin, nMax + 1):
        if i in primes:
            continue
        # find divisors
        divisors_results = []
        j = 1
        while j * j <= i:
            if i % j == 0:
                divisors_results.append(j)
                if i // j != j:
                    divisors_results.append(i // j)
            j += 1
                
        # find the sum of divisors
        sum_of_divisors = sum(divisors_results)

        # find prime factors
        n = i
        factors = []
        counter = 0

        while n > 1:
            while n % primes[counter] == 0:
                factors.append(primes[counter])
                n //= primes[counter]
            counter += 1

        # find the sum of the factors
        sum_of_factors = sum(factors)

        # add number to the list if property checks out
        if sum_of_divisors%sum_of_factors == 0:
            results.append(i)

    return results # sorted list
