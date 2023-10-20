a,b,c = map(int,input().split())
result = []
for i in a,b,c :
    result.append(i)

result.sort()
print(result[1])