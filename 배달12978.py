from collections import defaultdict
import heapq
def ekdlrtmxmfk(roads,root,N):
    visited =[1e9]*(N+1)
    
    stack= [[0,root]]
    visited[root] = 0
    hq = heapq.heapify(stack)
    hq = stack
    while hq:
        #print(hq, visited)
        pop = heapq.heappop(hq)
        if visited[pop[1]] < pop[0]:
            continue
        for b in roads[pop[1]]:  
            if visited[pop[1]] + b[1] <visited[b[0]]:
                visited[b[0]] = visited[pop[1]] + b[1]
                heapq.heappush(hq,[visited[pop[1]] + b[1],b[0]])
    return visited
        
        
    
def solution(N, road, K):
    answer = 0
    roads = defaultdict(list)
    for a in road:
        roads[a[0]].append([a[1],a[2]])
        roads[a[1]].append([a[0],a[2]])
    #print(roads)
    #print(roads[1])
    cnt =0
    for a in ekdlrtmxmfk(roads,1,N):
        if a<=K:
            cnt +=1
    
    return cnt