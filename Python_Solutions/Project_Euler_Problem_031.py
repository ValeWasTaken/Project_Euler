def main():
    coins = [1,2,5,10,20,50,100,200]
    goal = 200
    ways = ([1]+[0] * goal)

    for x in coins:
        for i in range(x, goal+1):
            ways[i] += ways[i-x]
        
    print ways[goal]
main()
