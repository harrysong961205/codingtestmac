import itertools
def solution(word):
    answer = 0
    alp = ["A","E","I","O","U"]
    list_all = set()
    for a in itertools.product(alp):
        list_all.add(a[0])
    for a in itertools.product(alp,alp):
        list_all.add(a[0]+a[1])
    for a in itertools.product(alp,alp,alp):
        list_all.add(a[0]+a[1]+a[2])
    for a in itertools.product(alp,alp,alp,alp):
        list_all.add(a[0]+a[1]+a[2]+a[3])
    for a in itertools.product(alp,alp,alp,alp,alp):
        list_all.add(a[0]+a[1]+a[2]+a[3]+a[4])
    return sorted(list(list_all)).index(word)+1
    
    