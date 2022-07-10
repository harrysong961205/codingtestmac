def solution(numbers, target):
    whole =[]
    cnt =0
    for a in range(len(numbers)):
        if a == 0:
            whole.append(numbers[0])
            whole.append(-numbers[0])
        else:
            new =[]
            for b in whole:
                new.append(b + numbers[a])
                new.append(b - numbers[a])
            whole =new

    return whole.count(target)