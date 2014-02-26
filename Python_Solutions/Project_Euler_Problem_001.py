#Project Euler - Problem 1: Multiples of 3 and 5
#Goal: Find the sum of all the multiples of 3 or 5 below 1000.
#Date of completion: 1/2/2014
def main():
    answer = 0
    for x in range(1000): # Uses X to check numbers up to 1000.
        if (x % 5 == 0 or x % 3 == 0):
            answer = answer + x
    print answer #Prints sum of all multiples of 3 or 5 below 1000.
main()
