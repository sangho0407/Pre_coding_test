
price = []
for i in range(10) :
    n = int(input())
    price.append(n)
total_price = price[0]
price.remove(price[0])
print(total_price-sum(price))



