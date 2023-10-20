n,m,k = map(int,input().split())

date = list(map(int,input().split()))

date.sort()

first = date[::-1][0]
secend = date[::-1][1]

result = 0

while True :
    for i in range(k) :
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0 :
        break
    result += secend
    m -= 1

print(result)