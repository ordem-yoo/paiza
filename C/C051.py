# 카드 1 ~ 9 까지 4장만 사용
# 카드 중복되는 경우 있음
# 2장씩 묶어 숫자를 더함

selectCard = list(map(int, input().split()))
firstMax = max(selectCard)
selectCard.remove(firstMax)
secondMax = max(selectCard)
selectCard.remove(secondMax)
result = 10*(firstMax+secondMax)+selectCard[0]+selectCard[1]
print(result)