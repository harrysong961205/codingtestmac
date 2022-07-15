def rotation(a,whole):
    arr = []
    now = [a[0]-1,a[1]-1]
    while now != [a[0]-1,a[3]-1]:
        now[1] +=1
        app = now[:]
        arr.append(app)
    while now != [a[2]-1,a[3]-1]:
        now[0] +=1
        app = now[:]
        arr.append(app)
    while now != [a[2]-1,a[1]-1]:
        now[1] -=1
        app = now[:]
        arr.append(app)
    while now != [a[0]-1,a[1]-1]:
        now[0] -=1
        app = now[:]
        arr.append(app)
    
    min_arr = []
    insert = whole[a[0]-1][a[1]-1]
    for a in arr:
        
        hold = whole[a[0]][a[1]]
        whole[a[0]][a[1]] = insert
        min_arr.append(insert)
        insert = hold
    #for a in whole:
        #print(a)
    return min(min_arr)
def solution(rows, columns, queries):
    answer = []
    whole = []
    cnt =1 
    for a in range(rows):
        whole.append([])
        for b in range(columns):
            whole[a].append(cnt)
            cnt+=1
    for a in queries:
        answer.append(rotation(a,whole))
        
    
        
        
    return answer