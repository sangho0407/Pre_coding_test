def solution(arr, k):
    answer = []
    for num in arr:
        if num not in answer:
            answer.append(num)
            
    while len(answer) < k:
        answer.append(-1)
    
    return answer[:k]