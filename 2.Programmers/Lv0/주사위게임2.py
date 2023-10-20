
def solution(a, b, c):
    answer = 0
    if  a ==b and b==c and a==c :
        answer += (a + b + c) * (a **2 + b **2 + c **2) * (a **3 + b **3 + c **3)
    elif a ==b or b==c or a==c :
        answer += (a + b + c) * (a **2 + b **2 + c **2) 

    else :
        answer += (a + b + c)
    return answer

# 한 수 배우는 코드
'''
set 활용 중복값 제거 후 len으로 체크하는 방법도 있음

def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)
        
'''