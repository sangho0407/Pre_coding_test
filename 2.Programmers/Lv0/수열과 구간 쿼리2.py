def solution(arr, queries):
    answer = []
    for s,e,k in queries :
        nums = []
        for i in range(s,e+1): 
            if arr[i] > k :
                nums.append(arr[i])
        if nums :
            answer.append(min(nums))
        else : 
            answer.append(-1)
    return answer