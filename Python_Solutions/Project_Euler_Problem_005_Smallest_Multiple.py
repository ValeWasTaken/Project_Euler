def main():
    x = 0
    while(x != -1):
        x += 20
        if all(x % k == 0 for k in range(1, 21)):
            print(x)
            return 0
main()
