import math
import collections
from collections import deque
def solution(progresses, speeds):
    answer = []
    days = []
    for a in range(len(speeds)):
        days.append(math.ceil((100 - progresses[a])/speeds[a]))
    print(days)
    stack = deque([])
    for a in range(len(days)):
        if len(stack)  == 0:
            print("new")
            stack.append(days[a])
        else:
            if stack[-1] >= days[a]:
                stack.appendleft(days[a])
            else:
                print("next day")
                answer.append(len(stack))
                stack = deque([days[a]])
        print(stack)
    answer.append(len(stack))
            
    return answer