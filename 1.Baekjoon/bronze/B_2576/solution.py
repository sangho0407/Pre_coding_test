num = []
result = []
for _ in range(7) :
    n = int(input())
    num.append(n)

for i in num :
    if i % 2 != 0 :
        result.append(i)
if not result :
    print(-1)
else :
    print(sum(result),min(result),sep='\n')