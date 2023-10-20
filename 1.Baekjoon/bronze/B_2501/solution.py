result = []
k,n = map(int,input().split())

for i in range(1,k+1) :
    if k % i == 0 :
        result.append(i)

try :
    print(result[n-1])
except IndexError :
    print(0)
