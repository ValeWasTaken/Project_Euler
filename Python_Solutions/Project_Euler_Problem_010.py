# Python 3.4
def sum_primes(limit=1999999):
    answer = 0
    
    # Sieve of Eratosthenes
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if sieve[num]:
           answer += num
           for i in range(num * num, limit + 1, num):
               sieve[i] = False
    return answer
sum_primes()
