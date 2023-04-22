# 날짜 입력,구매 기준가 입력 (1주), 판매 기준가 입력 (모두)
# 기준가와 판매가 사이는 아무것도 안함
# 입력한 날짜에는 전부 판매

date, buy_price, sell_price = map(int, input().split())
stock,result = 0, 0

for i in range(date) :
    intput_price = int(input())
    if intput_price >= sell_price or i == date - 1 :
        result += intput_price * stock
        stock = 0
    elif intput_price <= buy_price : 
        result += -intput_price
        stock += 1
print(result)
