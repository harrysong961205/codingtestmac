def solution(s, skip, index):
    answer = ''
    skip = [ord(a) for a in skip]
    #print(skip)
    for a in s:
        alps = []
        for b in range(1,index+1):
            row_ord = ord(a)+b
            if row_ord <= 122:
                alps.append(row_ord)
            else:
                alps.append(row_ord -26)
        #print([chr(a) for a in alps])
        jump_len = index - (len(set(alps) - set(skip)))
        #print(chr(alps[-1]+jump_len-26),jump_len)
        r = alps[-1]+jump_len if alps[-1]+jump_len <= 122 else alps[-1]+jump_len -26
        while r in skip:
            if r <=122:
                r+=1
            else:
                r -= 26
        answer +=chr(r)
    return answer