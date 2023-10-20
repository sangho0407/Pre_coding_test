import sys
k,l = input().split()

for i in range(2,int(l)):
    if int(k) % i == 0:
        print("BAD", int(i))
        exit()

print('GOOD')