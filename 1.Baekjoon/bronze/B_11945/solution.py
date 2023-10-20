a,b = map(int,input().split())
result = []
for i in range(a):
    fig = str(input())
    result.append(fig[::-1])

for i in result :
    print(i)