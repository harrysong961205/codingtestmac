def solution(maps):
    answer = []
    w,h = len(maps[0]),len(maps)
    d = {"u":[-1,0],"d":[1,0],"l":[0,-1],"r":[0,1]}
    done = []
    def do_live(maps,a,b):
        days = 0
        stack=[[a,b]]
        while stack:
            poped = stack.pop()
            done.append(poped)
            days += int(maps[poped[0]][poped[1]])
            for move in d:
                try:
                    print(maps[poped[0]+d[move][0]][poped[1]+d[move][1]])
                    if 0<=poped[0]+d[move][0]<= h and 0<=poped[1]+d[move][1]<= w and maps[poped[0]+d[move][0]][poped[1]+d[move][1]] != "X" and not [poped[0]+d[move][0],poped[1]+d[move][1]] in done and not [poped[0]+d[move][0],poped[1]+d[move][1]] in stack:
                        stack.append([poped[0]+d[move][0],poped[1]+d[move][1]])
                        
                except:
                    pass
        return days
                        
                
    for a in range(len(maps)):
        for b in range(len(maps[a])):
            if (maps[a][b] != "X") and ([a,b] not in done):
                w_d = do_live(maps,a,b)
                answer.append(w_d)
                
    if answer ==[]:
        return [-1]
    return sorted(answer)