def dfs(wait_room):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    okay = True
    
    for a in range(5):
        for b in range(5):
            if wait_room[a][b] == "O":
                cnt = 0
                for c in range(4):
                    if 0<=a+dx[c]<=4 and 0<= b+dy[c]<=4:
                        ard = wait_room[a+dx[c]][b+dy[c]]
                        if ard =="P":
                            cnt+=1
                    if cnt>=2:
                        okay=False
            elif wait_room[a][b] == "P":
                for c in range(4):
                    if 0<=a+dx[c]<=4 and 0<= b+dy[c]<=4:
                        ard = wait_room[a+dx[c]][b+dy[c]]
                        if ard =="P":
                            okay=False
                            
    return [wait_room, okay]
def solution(places):
    answer = []
    for a in range(len(places)):
        if dfs(places[a])[1]:
            answer.append(1)
        else:
            answer.append(0)
            
        
        
        
    
    
    return answer