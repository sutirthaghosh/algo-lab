no_of_inversions = 0
def merge(a,b):
    """ Function to merge two arrays """
    global no_of_inversions
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] <= b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            no_of_inversions += len(a) 
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

# Code for merge sort

def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x)/2)
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)
    

if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print (mergesort(arr))
    print("Number of Inversions = ",no_of_inversions)
