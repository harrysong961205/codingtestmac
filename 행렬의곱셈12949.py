import numpy as np
def solution(arr1, arr2):
    answer = [[]]
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    try:
        return np.dot(arr1,arr2).tolist()
    except:
        pass
    return answer