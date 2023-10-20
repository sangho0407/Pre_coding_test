import sys

n = int(sys.stdin.readline())
result = 0

for _ in range(n):
    m = int(sys.stdin.readline())
    result += m

print(result-n+1)