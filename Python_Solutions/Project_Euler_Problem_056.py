# Python 2.7

def digit_sum():
    max_digit_sum = 0
    for a in xrange(1,101):
        digit_sum = 0
        for b in xrange(1,101):
            number_sum = str(a**b)
            digit_sum = 0
            for number in number_sum[::]:
                digit_sum += int(number)
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum
    print(max_digit_sum)
digit_sum()
