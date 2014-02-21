#Date completed: 1/2/2014
def main():
    a = 0 #
    b = 1 # Defines variables that will be used in the program
    c = 0 # And assigns needed values for the formula.
    d = 0 #
    while (c < 3500000): # While C is less than 3.5mil, execute the below code
        c = a + b #Calculates Fibonacci sequence starting with: 0,1,1,..
        print c #Displays the current number in the sequence being counted
        a = b # Starts the process of moving onto the next number in the sequence
        b = c # Completes the sequence
        if (c % 2 == 0): #If C is evenly divisable by 2 execute below code.
            d = d + c #Stores the even fibonacci value for the later sum of all evens.
    print("The highest fibonacci value under 4million is: " + str(c)) #Displaysthe last even fib. num under 4mil
    print("The sum of all EVEN fibonacci values under 4million is: " + str(d)) #Displays the sum of all even fib. numbers
main() #Runs the program
