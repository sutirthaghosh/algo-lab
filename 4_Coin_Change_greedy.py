import math
if __name__ == '__main__':
    coins = input()
    coins = [int(i) for i in coins.split()]
    total = int(input())
    temp = total
    coins.sort(reverse = True)
    i = 0
    while temp > 0 and i < len(coins):
        print("No of coins of type ",coins[i]," = ",math.floor(temp/coins[i]))
        temp -= coins[i] * math.floor(temp/coins[i])
        i += 1

