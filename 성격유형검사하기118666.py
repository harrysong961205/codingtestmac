import collections
def solution(survey, choices):
    answer = ''
    dict1 = collections.defaultdict(lambda : 0)
    for a in range(len(survey)):
        fir,sec = survey[a][0], survey[a][1]
        now_cho = choices[a] -4
        if 0==now_cho:
            continue
        elif 0<now_cho:
            dict1[sec]+= now_cho
        else:
            dict1[fir]+= -now_cho
    types = ["R","T","C","F","J","M","A","N"]
    for a in types:
        try:
            test=dict1[a] 
        except:
            dict1[a] = 0
    for a in range(0,len(types),2):
        if dict1[types[a]] <dict1[types[a+1]]:
            answer+=types[a+1]
        else:
            answer+= types[a]
    return answer