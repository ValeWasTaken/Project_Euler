# Project Euler Problem 48 - Self Powers
# Find the 10 digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def main():
    total = 0
    for x in range(1, 1001):
        total += x**x
    print str(total)[-10:] #Prints the last 10 digits of the total.
main()

#Note: This solution could be one line by using the following below code.
#However, I did not come up with it, nor do I like it as much as my solution due to readability reasons.
#print(str(sum([x**x for x in range(1,1001)]))[-10:])
