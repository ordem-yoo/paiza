buyCount, availableSaleItem, saleItem = map(int, input().split())
shoppingList = [0 for i in range(buyCount)]
result = 0

for i in range(buyCount) :
    shoppingList[i] = int(input())
shoppingList.sort()
if buyCount >= availableSaleItem :
    for i in range(saleItem, buyCount) :
        result += shoppingList[i]
else :
    for i in range(buyCount) :
        result += shoppingList[i] 
print(result)