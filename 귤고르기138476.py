import collections
def solution(k, t):
    kind = 0
    t = collections.Counter(t).most_common()
    for i in t:
        k -= i[1]
        kind +=1
        if  k<= 0:
            break
    return kind