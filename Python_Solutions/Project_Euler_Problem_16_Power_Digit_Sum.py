# Project Euler Problem 16 - Power Digit Sum
# Find the sum of the digits of 2^1000

def main():
    original_num = str(2**1000) #2 ^ 1000
    sum_of_digits = 0

    for digit in original_num:
        sum_of_digits = sum_of_digits + int(digit)

    print(sum_of_digits)
main()
