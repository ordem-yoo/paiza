# 공격, 방어, 민첩 -> 진화에 해당하는 조건 입력
# 몬스터 수 입력
# 몬스터 이름, 최소공, 최대공, 최소방, 최대방, 최소민, 최대민
# 진화 가능한 몬스터 출력
# 없으면 no evolution

attack, deffence, agility = map(int, input().split())
count = int(input())
monsterInfo = [[] for i in range(count)]
evolutionMonster = []
for i in range(count) :
    monsterInfo[i] = list(map(str,input().split()))
    if attack in range(int(monsterInfo[i][1]),int(monsterInfo[i][2])+1) and deffence in range(int(monsterInfo[i][3]),int(monsterInfo[i][4])+1) and agility in range(int(monsterInfo[i][5]),int(monsterInfo[i][6])+1) :
        evolutionMonster.append(monsterInfo[i][0])

if len(evolutionMonster) == 0  :
    print("no evolution")
else :
    for i in range(len(evolutionMonster)) :
        print(evolutionMonster[i])