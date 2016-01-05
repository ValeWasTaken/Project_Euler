def problem_007(limit=104750):
    answer = 0
    
    # Sieve of Eratosthenes
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if sieve[num]:
           answer = num
           for i in range(num * num, limit + 1, num):
               sieve[i] = False

    return answer
print(problem_007())
