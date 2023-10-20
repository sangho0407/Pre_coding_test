n = int(input())
cnt = 1
six = 6
count = 1
while n > cnt:
    count += 1
    cnt += six
    six += 6
print(count)
