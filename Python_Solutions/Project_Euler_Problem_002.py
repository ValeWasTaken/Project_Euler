def main():
    a,b,c,d = 0,1,0,0 
    while (c < 3500000): 
        c = a + b
        a = b
        b = c
        if (c % 2 == 0):
            d += c
    print("The highest fibonacci value under 4million is: " + str(c)) 
    print("The sum of all EVEN fibonacci values under 4million is: " + str(d))
main() 
