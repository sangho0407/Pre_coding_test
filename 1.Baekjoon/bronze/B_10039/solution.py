
sum = 0

for i in range(5) :
    n = int(input())
    if n <= 40 :
        n = 40
        sum += n
    else :
        sum += n

print(int(sum/5))