import itertools
from itertools import permutations
def sosu(x):
    if x == 1 or x == 0:
        return False
    for a in range(2,x):
        if x%a==0:
            return False
    return True


def solution(numbers):
    is_sosu=0
    num_list = []
    for a in range(len(numbers)):
        num_list.append(numbers[a])
    mix_num=[]
    for b in range(1,len(num_list)+1):
        list1 =list(itertools.permutations(num_list,b))

        aa=""
        for c in list1:
            aa=""
            for e in c:
                aa += str(e)
            mix_num.append(aa)
    sosu_list = set(map(int,mix_num))
    sosu_num = 0
    for q in sosu_list:
        if sosu(q):
            sosu_num +=1
            print(q)

    
    return sosu_num