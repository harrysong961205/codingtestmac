def solution(today, terms, privacies):
    answer = []
    def trans(date):
        date = date.split(".")
        return (int(date[0])-2000)*12*28 + int(date[1])*28 + int(date[2])
    today = trans(today)
    dict_d = {}
    for a in terms:
        t = a.split(" ")
        dict_d[t[0]] = int(t[1])*28
    for p in range(len(privacies)):
        _p = privacies[p].split(" ")
        if trans(_p[0])+dict_d[_p[1]]-1 < today:
            answer.append(p+1)
    return answer