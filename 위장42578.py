def solution(clothes):
    dict = {}
    for a in clothes:
        if a[1] in dict:
            clt_list = list(dict.get(a[1]))
            clt_list.append(a[0])
            dict[a[1]] = clt_list
        else:
            dict[a[1]] = [a[0]]
    combination = 1
    for b in list(dict.keys()):
        combination *= (len(dict.get(b))+1)
    answer = combination-1
    return answer