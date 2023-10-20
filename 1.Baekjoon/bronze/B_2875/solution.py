n, m, k = map(int, input().split())
temp = 0
while True:
    n = n - 2
    m = m - 1
    if n < 0 or m < 0 or (n+m) < k:
        break
    temp += 1
print (temp)