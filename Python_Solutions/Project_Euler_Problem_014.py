# Project Euler Problem 14 - Python 3.4

def longest_collatz():
    longest_chain, answer = 0, 0
    for n in range(1,1000000,2):
        longest_collatz = n
        count = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = (n * 3) + 1
            count += 1
        if count > longest_chain:
            longest_chain = count
            answer = longest_collatz
    print('Number producing largest chain: '\
          '{0} \nChain size: {1}'.format(answer, longest_chain))
