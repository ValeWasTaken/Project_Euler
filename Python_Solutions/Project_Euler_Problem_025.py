def main():
    x,y,z = 0,1,0
    counter = 1
    while len(str(z)) != 1000:
        z = x + y
        x = y 
        y = z 
        counter += 1
    print("The " + str(counter) + "nd number in the Fibonacci sequence produces the first 1000 digit number.") 
    # Expected output: 4782
main()
