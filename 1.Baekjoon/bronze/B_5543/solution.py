

buger = []
drink = []
result = 0
for _ in range(3) :
    n = int(input())
    buger.append(n)
for _ in range(2) :
    m = int(input())
    drink.append(m)

print(min(buger) + min(drink) - 50) 