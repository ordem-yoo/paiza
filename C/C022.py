stock_price_table = []

while True :
    date = int(input())
    if date < 1 or date > 1000 :
        continue
    else :
        break

for i in range(date) :
    stock_price_table.append(list(map(int, input().split())))
best_price = stock_price_table[0][-2]
worst_price = stock_price_table[0][-1]

for i in range(1,date):
    if best_price < stock_price_table[i][-2]:
        best_price = stock_price_table[i][2]
    if worst_price > stock_price_table[i][-1]:
        worst_price = stock_price_table[i][-1]
        
print(stock_price_table[0][0],stock_price_table[-1][1],best_price,worst_price)