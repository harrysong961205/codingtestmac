def solution(name):
    answer = 0
    for a in name:
        if a == "A":
            continue
        min_Alp = min(ord(a)-65,91-ord(a))
        answer +=min_Alp
    print("sumAlp : ",answer)
    not_a = []
    for a in range(len(name)):
        if name[a]!="A":
            not_a.append(a)
            print(name[a],a)
    print(not_a)
    cross = []
    for a in range(len(not_a)-1):
        if not_a[a] ==0:
            first = 0
        else:
            first = not_a[a]
        if not_a[a+1] == len(name)-1:
            last = 0
        else:
            last = len(name)-1 - not_a[a+1]
        
        whole_len= min(2*first + last+1,1+2*last+1+first)
        cross.append(whole_len)
        print(first,last , whole_len)
    if not_a != []:
        cross.append(not_a[-1])
    else:
        cross.append(0)
    
    print(cross, "cross",min(cross))
    answer+= min(cross)
    print(answer)
    
    #print(not_a)
            
    return answer