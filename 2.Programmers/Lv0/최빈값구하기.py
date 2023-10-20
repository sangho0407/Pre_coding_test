from collections import Counter

def solution(array):
    cnt = Counter(array)
    most_common = cnt.most_common(2)
    print('most_common=',most_common)
    if len(most_common) == 1 or most_common[0][1] != most_common[1][1]:
        return most_common[0][0]
    else:
        return -1