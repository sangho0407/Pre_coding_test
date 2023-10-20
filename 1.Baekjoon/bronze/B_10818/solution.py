import sys

P_num = sys.stdin.readline().rstrip().split()
P_num = list(map(int,sys.stdin.readline().rstrip().split()))
item_list = []
for i in P_num :
    item_list.append(i)
    
print(min(item_list),max(item_list),end=" ")