def solution(numbers, n):
    answer = 0
    
    for idx, num in enumerate(numbers):
        answer += num
        if answer > n:
            return answer
        
    return answer