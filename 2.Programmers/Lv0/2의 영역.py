def solution(arr):
    first_idx = -1
    last_idx = -1
    
    for idx, num in enumerate(arr):
        if num == 2:
            if first_idx == -1 :
                first_idx = idx
            last_idx = idx
            
    if first_idx == -1:
        return [-1]
    
    return arr[first_idx:last_idx+1]


#한 수 배우는 코드

'''

def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]

'''