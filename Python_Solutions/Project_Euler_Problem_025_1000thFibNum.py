def main():
    x,y,z = 0,1,0
    counter = 1
    while len(str(z)) != 1000: #Length counter
        z = x + y #
        x = y # Fibonacci sequence
        y = z #
        counter += 1
    # Add "print z" to display the 1000 digit number.
    # When checking num it should be: 10700...816
    print("The " + str(counter) + "nd number in the Fibonacci sequence produces the first 1000 digit number.")
    # counter, the number printed, should be '4782'.
main()
