def main():
    #Start of square of sums block
    n = 0
    for x in range(1,101): # Counting 1-100
        n = n + x # Adding values of 1-100
    final_n = n**2 # Squaring sum of 1-100
    print("The square of the sum of the first 100 natural numbers is: "+str(final_n)) 

    #Start of sum of squares block
    num = 0
    for y in range(1,101):
        num = num + y**2
    final_num = num
    print("The sum of the squares of the first 100 natural numbers is: "+str(final_num))

    #Final calculation
    difference = final_n - final_num
    print("The difference between the two sums is: "+str(difference))
    
main()
