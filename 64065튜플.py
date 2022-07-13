def solution(s):
    answer = []
    w = s.split("},")
    for a in w:
        a=a.replace("{","")
        a = a.replace("}","")
        answer.append(a)
    
    answer1 = []
    for a in answer:
        if a == "":
            pass
        else:
            answer1.append(a)
    real_answer = []
    for a in answer:
        cnt =0
        for b in range(len(a)):
            if a[b] == ",":
                cnt+=1
        real_answer.append([a,cnt])
    last = []
    whole = []
    for a in sorted(real_answer,key = lambda x:x[1]):
        a=a[0].split(",")
        for b in a:
            if b not in whole:
                whole.append(b)
    for a in range(len(whole)):
        whole[a] = int(whole[a])
        
    
        

        
    return whole