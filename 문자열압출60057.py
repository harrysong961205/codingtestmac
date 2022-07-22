def solution(s):
    if len(s)==1:
        return 1
    answer = 1e7
    start =0
    for a in range(1,len(s)):
        start = 0
        end = a
        inv_list = []
        while end  <= a+len(s):
            try:
                inv_list.append(s[start:end])
                start += a
                end += a
            except:
                end = len(s)-1
                start = len(s)-1-(len(s)%a)
                inv_list.append(s[start:end])
                #print("y")
        if inv_list[-1] == "":
            inv_list.pop()
        stack = [[inv_list.pop(0),1]]
        for c in inv_list:
            if stack[-1][0] == c:
                stack[-1] = [c,stack[-1][1]+1]
            else:
                stack.append([c,1])
        #print(stack)
        last = ""
        for q in stack:
            if q[1] == 1:
                last += q[0]
            else:
                last +=str(q[1]) +q[0]
        if len(last) <answer:
            answer = len(last)
    return answer