# 최초 금액과 하차 횟수 입력
# 각 횟수에 들어가는 교통비 입력
# 적립은 10%씩 적립

# 출력은 남은 금액과 마일리지가 얼만큼 적립되었는지 출력
# 잔액은 1원부터 만원까지
# 횟수는 1부터 100까지
# 버스 비용은 10의 배수, 0원부터 만원까지

while True :
    wallet, count = map(int, input().split())
    if wallet < 1 or wallet > 10000 or count < 1 or count > 100 :
        continue
    else :
        break
    
price = [ 0 for i in range(count) ]
point = [ 0 for i in range(count) ]
record = [ 0 for i in range(count) ]

for i in range(count) :
    while True:
        price[i] = int(input())
        if price[i] < 0 or price[i] > 10000 or price[i] % 10 != 0 :
            continue
        else :
            break

for i in range(count) :
    if i == 0 : # 0번 만
        wallet -= price[i]
        point[i] = int(price[i] / 10)
    else : # 1번째 부터
        if price[i] > point[i-1] :
            wallet -= price[i]
            point[i] = point[i-1] + int(price[i] / 10)
        else : 
            point[i] = point[i-1] - price[i]
    record[i] = wallet

for i in range(count) :
    print(record[i], point[i])