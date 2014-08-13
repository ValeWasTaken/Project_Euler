def main():
    answer = 0
    for x in range(1000): # Uses X to check numbers up to 1000.
        if (x % 5 == 0 or x % 3 == 0):
            answer += x
    print answer #Prints sum of all multiples of 3 or 5 below 1000.
main()
