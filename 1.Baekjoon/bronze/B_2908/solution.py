# a,b입력받아서 역순으로 정렬 734 = 437 , 893 = 398
# 역순정렬된 두 수중 더 큰 수를 출력

a,b = list(map(str,input().split()))

ra = a[::-1]
rb = b[::-1]

if ra > rb :
    print(ra)
else :
    print(rb)