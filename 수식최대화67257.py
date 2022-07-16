import re
import itertools
from itertools import permutations
def do_math(a,b):
    if a =="-":
        try:
            index = b.index("-")
            new = int(b[index -1]) - int(b[index +1])
            b.pop(index-1)
            b.pop(index-1)
            b.pop(index-1)
            b.insert(index-1,new)
            return b
        except:
            return b
    if a =="*":
        try:
            index = b.index("*")
            new = int(b[index -1]) * int(b[index +1])
            b.pop(index-1)
            b.pop(index-1)
            b.pop(index-1)
            b.insert(index-1,new)
            return b
        except:
            return b
    if a =="+":
        try:
            index = b.index("+")
            new = int(b[index -1]) + int(b[index +1])
            b.pop(index-1)
            b.pop(index-1)
            b.pop(index-1)
            b.insert(index-1,new)
            return b
        except:
            return b
def solution(expression):
    answer = []
    whole = []
    nums = []
    giho = []
    number = ''
    for a in range(len(expression)):
        if expression[a] == "-" or expression[a] == "+" or expression[a] == "*":
            giho.append(expression[a])
            nums.append(number)
            number = ''
        else:
            number +=expression[a]
    nums.append(number)
    perm = itertools.permutations(set(giho))
    for a in range(len(giho)):
        whole.append(nums[a])
        whole.append(giho[a])
    whole.append(nums[-1])
    
    print(whole)
    
    for a in perm:
        now_whole = whole[:]
        print(now_whole)
        for b in a:
            while b in now_whole:
                now_whole = do_math(b,now_whole)
                
        answer.append(abs(now_whole[0]))
        
    return max(answer)