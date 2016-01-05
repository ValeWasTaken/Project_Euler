def problem_005():
    x = 0
    while True:
        x += 20
        if all(x % k == 0 for k in range(1, 21)):
            return x
print(problem_005())
