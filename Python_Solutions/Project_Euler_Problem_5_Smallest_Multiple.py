def main():
    x = 1
    while(x != 0):
        x = x + 1
        if all(x % k == 0 for k in range(1, 21)):
            print(x)
            return 0
main()

# Note to self 
# Please optimize this code at a later date, it currently takes far more processing power than is optimal.
