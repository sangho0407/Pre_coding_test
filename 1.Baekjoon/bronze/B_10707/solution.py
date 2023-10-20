p_list = []
for i in range(5) :
    n = int(input())
    p_list.append(n)

x = p_list[0]*p_list[4]

if p_list[4] <= p_list[2] :
    y = p_list[1]
else :
    y = ((p_list[4] - p_list[2])*p_list[3]) + p_list[1]

if x < y : 
    print(x)
else :
    print(y)
