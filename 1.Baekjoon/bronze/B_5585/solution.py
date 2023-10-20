N = int(input())
coin = 1000 - N
arr = [500, 100, 50, 10, 5, 1]
result = 0

for i in arr:
    if coin == 0:
        break
    result += coin // i
    coin %= i
    
print(result)