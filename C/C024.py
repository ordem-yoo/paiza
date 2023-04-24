# set은 i번째 변수 에 값 a 를 대입(i = 1, 2)
# ADD는 변수 1의 값 + a를 계산하고 계산 결과를 변수 2에 할당
# SUB는 -a를 더하고 결과를 2에 넣기

a, b = 0, 0
while True :
    count = int(input())
    if count in range(1, 11):
        break
    else : 
        continue
log = [[]for i in range(count)]

for i in range(count) :
    log[i] = list(input().split())
    if log[i][0] == "SET" :
        if int(log[i][1]) == 1 :
            a = int(log[i][2])
        else :
            b = int(log[i][2])
    elif log[i][0] == "ADD" :
        b = a + int(log[i][1])
    elif log[i][0] == "SUB" :
        b = a - int(log[i][1])
print(a, b)