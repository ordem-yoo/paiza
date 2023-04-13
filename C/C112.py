"""

1 일차
a 에서 7시 출발 5시간 뒤에 12시 b에 도착  ( 시차 없음 )
-> a 에서 7시간 비행기 5시간 b에서 12시간 = 24시간


2일차
b에서 10시 출발 6시간 뒤에 c시간인 20시에 도착
-> b와 c는 시차가 있음 ( 4시간 )
-> b에서 10시간 비행기 6시간 c에서 4시간 = 20시간


3일차
c에서 12시 출발 3시간 뒤에 D에 도착
-> c와 d는 시차가 있음 ( 7시간 )
-> c에서 12시간 비행기 3시간 D에서 16시간 = 31시간


가장 짧은 시간과 가장 긴 시간을 차례로 출력

"""
while True:
    travel_day = int(input())
    if travel_day < 1 or travel_day > 100 :
        continue
    else :
        break

daytime=[ 0 for i in range(travel_day) ]

for i in range(travel_day) :
    while True:
        depart, stay, arrive = map(int,input().split())
        if depart < 1 or depart > 23 or stay < 1 or stay > 23 or arrive < 1 or arrive > 23 : 
            continue
        else:
            daytime[i] = depart + stay + 24-arrive    
            break
    
print(min(daytime))
print(max(daytime))