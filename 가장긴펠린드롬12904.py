def solution(s):
    answer = 0
    whole = []
    if len(s) == 1:
        return 1
    while len(s)!=0:
        
        find =True
        new_s = s[:]
        while find:
            if len(new_s)%2==0:
                #print(new_s[:int(len(new_s)/2)], new_s[int(len(new_s)/2):][::-1])
                if new_s[:int(len(new_s)/2)] == new_s[int(len(new_s)/2):][::-1]:
                    whole.append(len(new_s))
                    find= False
            else:
                #print(new_s[:int(len(new_s)/2)],new_s[int(len(new_s)/2)],  new_s[int(len(new_s)/2)+1:][::-1])
                if new_s[:int(len(new_s)/2)] == new_s[int(len(new_s)/2)+1:][::-1]:
                    whole.append(len(new_s))
                    find= False
            new_s = new_s[:len(new_s)-1]
            if len(new_s) ==1:
                break
        #print("----------",s)
        s = s[1:]
    if whole:
        return max(whole)
    return 1