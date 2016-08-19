if __name__ == '__main__':
    string = input()
    length = len(string)

    dp = [[0 for i in range(0, length)] for j in range(0, length)]
    path = [[ [0,0] for i in range(0, length)] for j in range(0, length)]
    for i in range(0, length):
        dp[i][i] = 1

    for i in range(0, length-1):
        if string[i] == string[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1

    for gap in range(2,length):
        for start,end in zip(range(0,length-gap),range(gap,length)):
            if string[start] == string[end]:
                dp[start][end] = dp[start+1][end-1] + 2
                path[start][end] = [1, -1,string[start]]
            else:
                if dp[start+1][end] > dp[start][end-1]:
                    path[start][end] = [1,0]
                    dp[start][end] = dp[start+1][end]
                else:
                    path[start][end] = [0, -1]
                    dp[start][end] = dp[start][end-1]

    pal_length = dp[0][length-1]
    result = ['X' for i in range(0,pal_length)]
    for i in range(0, length):
        print(dp[i])
    print("the LCPS path information ...")
    for i in range(0,length):
        print(path[i])
    '''start making result'''
    i = length-1
    j = 0
    begin = 0
    last = pal_length-1
    while i >= j:
        if path[j][i][0] == 1 and path[j][i][1] == -1:
            result[begin] = string[j]
            result[last] = string[j]
            begin += 1
            last -= 1
        if path[j][i][0] == 0 and path[j][i][1] == 0:
            result[begin] = string[j]
            result[last] = string[j]
            break
        temp = i
        i += path[j][i][1]
        j += path[j][temp][0]
    result = ''.join(result)
    print(result)