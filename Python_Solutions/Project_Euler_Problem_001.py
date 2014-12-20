def main():
    answer = 0
    for x in range(1000):
        if (x % 5 == 0 or x % 3 == 0):
            answer += x
    print answer
main()
