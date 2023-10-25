def solution(n):
    prime = []
    answer = []
    
    i = 2
    
    while i <= n:
        if n % i == 0 :
            prime.append(i)
            n = n//i
            
        else :
            i += 1
            
    for j in prime :
        if j not in answer :
            answer.append(j)
    return answer