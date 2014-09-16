def main():
    total = 0
    for x in range(1, 1001):
        total += x**x
    print str(total)[-10:]
main()
#Note: This solution could be one line by using the following below code.
#print(str(sum([x**x for x in range(1,1001)]))[-10:])
