import collections
def solution(genres, plays):
    answer = []
    answer_list = []
    dict1 = collections.defaultdict(list)
    for a in range(len(genres)):
        dict1[genres[a]].append([plays[a],a])
    for a in dict1:
        dict1[a] = sorted(dict1[a], key = lambda x:-x[0])
    
    for a in dict1:
        wp = 0
        for b in dict1[a]:
            wp +=b[0]
        dict1[a].append(wp)
    #print(dict1)
    for a in dict1:
        answer.append(dict1[a])
    answer = sorted(answer, key =lambda x:-x[-1])
    
    for a in answer:
        if len(a) >= 3:
            answer_list.append(a[0][1])
            answer_list.append(a[1][1])
        else:
            answer_list.append(a[0][1])
        
    return answer_list