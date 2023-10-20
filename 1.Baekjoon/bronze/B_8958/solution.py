K = int(input())

for _ in range(K) :
    ox_list = list(input())
    num = 0
    sum_num = 0
    for i in ox_list :
        if i == "O" :
            num += 1
            sum_num += num
        else :
            num = 0
    print(sum_num)

