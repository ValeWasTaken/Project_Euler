#Completed: 1/2/2014
def main():
    num = 600851475143 # You can replace this number with any number you want to find the largest prime to
    x = 2
    while x * x < num: #While less than the number cap, execute below code
        while num % x == 0: #If the generated number divides with no remainder execute below code
            num = num / x #Divide number by generated number (X) to get the prime number.
        x = x + 1 # Continue in formula searching for largest prime
    print num #Prints largest prime of the assigned number (600851475143)
main() #Execute program
