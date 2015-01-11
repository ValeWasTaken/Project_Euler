def reversible_numbers(limit):
        amount = 0
        for x in range(limit):
                y = int(str(x)[::-1])
                if len(str(x)) == len(str(y)):
                        total = x + y
                        temp = ''
                        for digit in str(total):
                                if int(digit) % 2 != 0:
                                        temp += str(digit)
                        if temp == str(total):
                                amount += 1
        print(amount)
reversible_numbers(input("Find reversible numbers below: "))
# Unoptimized solution -- Currently still a work-in-progress
