point = []
sum_point = []
for i in range(5) :
    n = list(map(int,input().split()))
    point.append(n)

for i in point :
    sum_point.append(sum(i))

print(sum_point.index(max(sum_point))+1,max(sum_point))