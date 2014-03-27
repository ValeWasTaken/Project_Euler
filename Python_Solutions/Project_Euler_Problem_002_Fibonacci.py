def main():
    a = 0 
    b = 1 
    c = 0 
    d = 0 
    while (c < 3500000): 
        c = a + b #Calculates Fibonacci sequence starting with: 0,1,1,..
        print c #Displays the current number in the sequence being counted
        a = b # Starts the process of moving onto the next number in the sequence
        b = c # Completes the sequence
        if (c % 2 == 0):
            d += c #Stores the even fibonacci value for the later sum of all evens.
    print("The highest fibonacci value under 4million is: " + str(c)) 
    print("The sum of all EVEN fibonacci values under 4million is: " + str(d))
main() 
