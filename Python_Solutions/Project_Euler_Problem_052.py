# Python 3.4
def permuted_multiples():
    for i in range(1,251749):
        base = sorted(str(i))
        multiples = [sorted(str(n*i)) for n in range(2, 7)]
            
        if all([base == m for m in multiples]):
            return i
