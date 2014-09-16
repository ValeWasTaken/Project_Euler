def is_prime(n):
    if n % 2 == 0: return False
    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True
 
def nth_prime(n):
    count,prime,iter = 1,2,3
    while count < n:
        if is_prime(iter):
            prime = iter
            count += 1
        iter += 2
    return prime

def main():
    desiredPrime = input("Enter the xth prime number you wish to find: ")
    print("the xth prime number you desired is: "+str(nth_prime(desiredPrime)))
main()
