#Date completed: 1/2/2014
def main():
    x = 0
    y = 1
    z = 0
    counter = 1
    while len(str(z)) != 1000: #Length counter
        z = x + y #
        x = y     # Fibonacci sequence
        y = z     #
        counter = counter + 1 #Term counter
    print z # Should be: 10700 ... 816
    print counter # Should be 4782
main()
