def bfs(arr,n,m):
    whole = []
    for a in arr:
        for b in range(n):
            done = True
            
            for c in range(m):
                if b ==a[c] or abs(b-a[c])==abs(m-c):
                    done=False
                    break
            if done:
                inv = a.copy()
                inv.append(b)
                whole.append(inv)
                
    
    return whole
            
def solution(n):
    arr =[]
    for a in range(n):
        arr.append([a])
    m =1
    for a in range(n-1):
        arr =bfs(arr,n,m)
        m+=1
        #print("----------------------")
    
    
    
    
        
    
    return len(arr)