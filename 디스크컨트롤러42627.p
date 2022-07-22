import heapq
import math
def solution(jobs):
    
    abs_time =[]
    time = 0
    bad_time = 0
    while len(jobs) !=0:
        wait = []
        for a in jobs:
            if time>=a[0]:
                wait.append([a[1],a[1]+time-a[0],a])
        heapq.heapify(wait)
        if wait == []:
            #doing = jobs.pop(0)
            #time +=doing[1]
            #abs_time.append(doing[1])
            time +=1
            
            #print("B")
            continue
        doing = heapq.heappop(wait)
        abs_time.append(doing[1])
        jobs.remove(doing[2])
        time += doing[2][1]
        #print(abs_time, doing, doing[0])
        
        
    return int(sum(abs_time)/len(abs_time))