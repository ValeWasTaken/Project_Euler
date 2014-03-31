#Project Euler Problem 31 - Coin Sums
#England currency has eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, 100p, and 200p
# How many ways can 200p be made using any number of coins?

def main():

    coins = [1,2,5,10,20,50,100,200]
    goal = 200
    ways = ([1]+[0] * goal)

    for x in coins:
        for i in range(x, goal+1):
            ways[i] += ways[i-x]
        
    print ways[goal]
main()
