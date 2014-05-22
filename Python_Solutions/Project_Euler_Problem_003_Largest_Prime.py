def main():
    num = 600851475143 
    x = 2
    while x * x < num: 
        while num % x == 0: 
            num /= x 
        x += 1
    print num #Prints largest prime of the assigned number (600851475143)
main()
