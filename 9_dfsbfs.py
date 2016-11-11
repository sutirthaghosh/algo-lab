from collections import deque

def bfs(graph, top):
    checked, queue = set(),[top]
    arr=[]
    while queue:
        vertex = queue.pop(0)
        #print (vertex, queue,checked,arr)
        if vertex not in checked:
            checked.add(vertex)
            arr.append(vertex)
            queue.extend(graph[vertex] - checked)
    return arr



def dfs(graph, top):
    checked, stack = set(), [top]
    arr=[]
    k=[]
    while stack:
        vertex = stack.pop()
        k=graph[vertex]
        l=[]
        m=set()
        for i in k:
            l.append(i)
        #l=list(reversed(l))
        for i in l:
            m.add(i)
        
        #print (vertex, stack,checked,arr)
        #print(l,m,k)
        if vertex not in checked:
            checked.add(vertex)
            arr.append(vertex)
            
            stack.extend(m - checked)
    return arr


graph = {'10': set(['5', '20']),
         '5': set(['10','1', '7']),
         '20': set(['10','15', '23']),
         '1': set(['5']),
         '7': set(['5']),
         '15': set(['20']),
         '23': set(['20'])}
         
#print (graph)

path=bfs(graph,'10')

print('BFS')
for i in path: 
    print(i,'-> ',end='')

print('END')


path=dfs(graph,'10')

print('DFS')
for i in path: 
    print(i,'-> ',end='')

print('END')
