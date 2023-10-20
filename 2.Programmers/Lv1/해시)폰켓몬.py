from collections import Counter
def solution(nums):
    a = Counter(nums)
    val = []
    for i,j in a.items():
        val.append(i)
    if len(val) >= len(nums)/2 :
        answer = len(nums)/2
    elif len(val) <= len(nums)/2 :
        answer = len(val)
    else :
        answer = len(val)
    return answer


'''
이것이 파이써닉이다..

def solution(ls):
    return min(len(ls)/2, len(set(ls)))

'''