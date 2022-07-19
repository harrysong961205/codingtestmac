def solution(skill, skill_trees):
    answer = -1
    cnt = 0
    skills = list(skill)
    print(skills)
    new_list = []
    for a in skill_trees:
        new = ''
        for b in range(len(a)):
            for c in skills:
                if a[b] == c:
                    new += c
        new_list.append(new)
    print(new_list)
    while "" in new_list:
        new_list.remove("")
        cnt+=1
    inv_list = []
    x = ''
    for a in skills:
        x +=a
        inv_list.append(x)
    print(inv_list)
    for a in new_list:
        for b in inv_list:
            if a == b:
                cnt +=1
                print(a,b)
    #print(cnt)
        
    return cnt