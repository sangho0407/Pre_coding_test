def solution(balls, share):
    n = 1
    m = 1
    nm = balls-share
    
    for i in range(1,balls+1) :
        n *= i
    for j in range(1,share+1):
        m *= j
    nm2 = 1
    for k in range(1,nm+1) :
        nm2 *= k
    return int(n/ (m*nm2))


    '''
    import math


def solution(balls, share):
    return math.comb(balls, share)
    
    '''