line = int(input())
result = []
for i in range(line) :
    n = int(input())
    result.append(n)

print(*sorted(result),sep='\n')