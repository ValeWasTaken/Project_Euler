def main():
    #Square of sums block
    n = 0
    for x in range(1,101):
        n += x
    final_n = n**2
    print("The square of the sum of the first 100 natural numbers is: "+str(final_n)) 

    #Sum of squares
    num = 0
    for y in range(1,101):
        num += y**2
    print("The sum of the squares of the first 100 natural numbers is: "+str(num))

    #Final calculation
    difference = final_n - num
    print("The difference between the two sums is: "+str(difference))
    
main()
