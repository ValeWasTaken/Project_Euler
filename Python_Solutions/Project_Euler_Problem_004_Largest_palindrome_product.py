def is_palindrome(number):
    return str(number) == str(number)[::-1]

if __name__ == "__main__":
    print('{} and {} => {}'.format(*max((i,j,i*j)
        for i in range(1000, 900, -1)
            for j in range(1000, 900, -1)
                if is_palindrome(i*j))))
