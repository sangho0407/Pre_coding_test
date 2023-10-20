n = int(input())
result = []
for i in range(n) :
    op = int(input())
    result.append(op)

cute = result.count(1)
not_cute = result.count(0)

if cute > not_cute:
    print("Junhee is cute!")
if not_cute > cute :
    print("Junhee is not cute!")

