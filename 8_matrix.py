
def MatrixChainOrder(p, n):    
    m = [[200000 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0    
    for L in range(2, n):
        for i,j in zip(range(1, n-L+1),range(L,n)):
            for k in range(i, j):             
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    ans[i][j]=k                 
    return m[1][n-1]


def sol(ans,lower,upper):
    if(lower==upper):
        
        print(" M"+str(lower)+"{"+str(arr[lower-1])+"X"+str(arr[lower])+"} ",end="")
    else:
        print("(",end="")
        sol(ans,lower,ans[lower][upper])
        if (ans[lower][upper]+1==upper and ans[lower][upper]==lower):
            print("*",end="")
        sol(ans,ans[lower][upper]+1,upper)
        print(")",end="")
           
    return


arr=[int(i) for i in input().split()]
#arr = [6,2,4,3,2]
size = len(arr)
ans = [[0 for x in range(size)] for x in range(size)]
print("Minimum number of multiplications is " +
       str(MatrixChainOrder(arr, size)))
for i in ans:
    print(i)
sol(ans,1,size-1)
print("")


