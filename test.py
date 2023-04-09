def solution(maps):
    answer = 0
    w,h = len(maps[0]),len(maps)
    for a in range(len(maps)):
        if "S" in maps[a]:
            for b in range(len(maps[a])):
                if maps[a][b] == "S":
                    start = [a,b]
        if "E" in maps[a]:
            for b in range(len(maps[a])):
                if maps[a][b] == "E":
                    end = [a,b]        
    dict1 = {"u":[0,1],"d":[0,-1],"l":[-1,0],"r":[1,0]}
    lever = []
    stack = [[start,0]]
    recent = []
    Done =False
    while stack:
        
        poped = stack.pop(0)
        recent.append(poped[0])
        for a in dict1:
            new_x = poped[0][0] + dict1[a][0]
            new_y = poped[0][1] + dict1[a][1]
            if (0 <= new_x< w) and (0 <= new_y< h) and (maps[new_x][new_y] !="X"):
                if [new_x,new_y] not in recent:
                    stack.append([[new_x,new_y],poped[1]+1])
                if maps[new_x][new_y] == "L":
                    Done = True
                    lever = [new_x,new_y]
                    answer += poped[1]+1
                    break
        if Done:
            break
                
    stack = [[lever,0]]
    recent = []
    while stack:
        
        poped = stack.pop(0)
        recent.append(poped[0])
        for a in dict1:
            new_x = poped[0][0] + dict1[a][0]
            new_y = poped[0][1] + dict1[a][1]
            if (0 <= new_x< w) and (0 <= new_y< h) and (maps[new_x][new_y] !="X"):
                if [new_x,new_y] not in recent:
                    stack.append([[new_x,new_y],poped[1]+1])
                if maps[new_x][new_y] == "E":
                    return poped[1]+1
                
    return -1