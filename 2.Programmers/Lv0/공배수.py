def solution(number, n, m):
    if number % n == 0 and number % m == 0 :
        return 1
    else :
        return 0
    
    
#한수 배우는 코드

#def solution(number, n, m):
#    return int(bool(number % n == 0) & bool(number % m == 0))