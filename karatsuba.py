
def karatsuba(x, y):
    print(x," ",y)
    if x < 10 or y < 10:
        print("RESULT = " ,x*y)
        return x*y
    max_length = max(len(str(x)), len(str(y)) )

    m2 = int(max_length/2)
    high1, low1 = int(str(x)[:m2]),int(str(x)[m2:])
    high2, low2 = int(str(y)[:m2]),int(str(y)[m2:])
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(high1+low1, high2+low2)
    z2 = karatsuba(high1, high2)
    result = (z2*(10 ** (2*m2)) )+( (z1-z2-z0) * 10 ** m2) + z0
    print("z0,z1,z2,m2,RESULT = ", result,z0,z1,z2,m2)
    return result

if __name__=='__main__':
    x=int(input())
    y=int(input())
    print(karatsuba(x,y))