import math
if __name__ == '__main__':
    coins = input()
    coins = [int(i) for i in coins.split()]
    total = int(input())
    temp = total
    coins.sort(reverse = True)

    table = [10000 for i in range(0,total+1)]
    table[0] = 0

    for i in range(1,total+1):
        for j in range(0,len(coins)):
            if i-coins[j] >= 0:
                table[i] = min(table[i],table[i-coins[j]]+1)

    print(table[total])