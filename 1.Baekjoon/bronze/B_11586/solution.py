n = int(input())
mirror = []
for i in range(n) :
    m = input()
    mirror.append(m)

feel = int(input())

if feel == 1 :
    print(*mirror,sep='\n')
if feel == 3 :  # 전체 거꾸로출력 --- 상하반전
    print(*mirror[::-1],sep='\n')
if feel == 2 : # i 원소를 거꾸로 출력 --- 좌우반전
    for i in mirror :
        print(i[::-1])