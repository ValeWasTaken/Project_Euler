#Project Euler - Problem 4
#Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):
    return str(number) == str(number)[::-1]

if __name__ == "__main__":
    print('{} and {} => {}'.format(*max((i,j,i*j)
        for i in range(1000, 900, -1)
            for j in range(1000, 900, -1)
                if is_palindrome(i*j))))

# The above I learned from watching a tutorial
# So below I decided to re-do the solution but instead to solve for
# The largest palindrome made from the product of two 4-digit numbers.

if __name__ == "__main__":
    print('{} and {} => {}'.format(*max((a,b,a*b)
        for a in range(10000, 9000, -1)
            for b in range(10000, 9000, -1)
                if is_palindrome(a*b))))
    
#Note: On line 18 & 19 the number "9000" can be lower, but is set at 9000
#because it is highly unlikely the number we are searching for will be
#lower than 9000 and if we include the lower numbers the procressing time
#and power required would be much higher for no reason.
