def solution(s):
    answer = True
    
    stack = []
    for a in range(len(s)):
        if len(stack) == 0:
            stack.append(s[a])
        else:
            if s[a] == "(":
                stack.append(s[a])
            else:
                if stack[-1] == "(":
                    stack.pop()
        #if ")" in stack:
            #return False
    if stack:
        return False
    return True
                
        

    return True