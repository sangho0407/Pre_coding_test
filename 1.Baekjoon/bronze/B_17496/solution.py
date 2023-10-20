
n,t,c,p = map(int,input().split())
day = []

for i in range(1,n+1,t):
    day.append(i)

if max(day) + t > n :
    del day[day.index(max(day))]

print(len(day)*c*p)