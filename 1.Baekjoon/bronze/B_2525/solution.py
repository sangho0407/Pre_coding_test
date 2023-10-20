t,m = map(int,input().split())
ad_m = int(input())

t += ad_m // 60
m += ad_m % 60

if m >= 60 :
      t += 1
      m -= 60
if t >= 24 :
      t -=24

print(t,m)