def solution(n):
    odd = []
    even =  []
    if n % 2 != 0 :
        for i in range(1,n+1) :
            if i % 2 != 0 :
                odd.append(i)
        return sum(odd)
    
    else:
        for j in range(1,n+1) :
            if j % 2 == 0 :
                even.append(j**2)
        return sum(even)


# 한 수 배우는 코드

'''
def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)
'''