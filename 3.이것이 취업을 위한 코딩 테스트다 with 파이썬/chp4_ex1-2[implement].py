n = int(input())
m = 60
s = 60
cnt = 0

for i in range(0,n+1):
    for j in range(m):
        for k in range(s):
            if '3' in str(i)+str(j)+str(k) :
                cnt += 1
print(cnt)