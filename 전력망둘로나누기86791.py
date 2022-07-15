import collections
def solution(n, wires):
    answer = -1
    result = []
    for a in wires:
        wire_new = wires[:]
        wire_new.remove(a) 
        dict1 =collections.defaultdict(list)
        for a in wire_new:
            dict1[a[0]].append(a[1])
            dict1[a[1]].append(a[0])
        #print(dict1)

        stack = [1]

        visited = [False] *n

        while stack:
            now = stack.pop()
            visited[now-1]=True
            for b in dict1[now]:
                if visited[b-1] == False:
                    stack.append(b)
        #print(visited)
        result.append(abs(visited.count(True)-visited.count(False)))
    


        
    
    
        
    return min(result)