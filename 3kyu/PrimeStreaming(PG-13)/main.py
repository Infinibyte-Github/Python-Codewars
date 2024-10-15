import itertools

class Primes:
    @staticmethod
    def stream():
        yield 2
        sieve = {}
        for num in itertools.count(3, 2):
            prime = sieve.pop(num, None)
            if prime is None:
                yield num
                sieve[num * num] = num
            else:
                next_multiple = num + 2 * prime
                while next_multiple in sieve:
                    next_multiple += 2 * prime
                sieve[next_multiple] = prime