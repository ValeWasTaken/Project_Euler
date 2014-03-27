# Project Euler Problem 48 - Self Powers
# Find the 10 digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def main():
    count = 1
    temp_num = 0
    total = 0
    while (count != 1000):
        temp_num = count**count
        total = total + temp_num
        count = count + 1
    total = str(total)
    print total[-10:]
main()
