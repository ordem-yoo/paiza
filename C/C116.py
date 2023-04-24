# 하루에 아이스크림 N 개 제조
# 아이스크림 막대에는 당첨과  꽝이 있음
# 아이스크림에서 꽝이 M회 연속으로 있는지 검사
# 하루에 5개 제조하면 3회 연속 꽝은 안되게 하려고 함
# 당첨은 1 꽝은 0

icecream, noLuck = map(int, input().split())
luckLog = list(input().split())
count = 0
status = False
for i in range(icecream) :
    if luckLog[i] == "0":
        count += 1
    else :
        count = 0
    if count >= noLuck :
        status = True
if status == True :
    print("NG")
else :
    print("OK")