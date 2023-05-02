houseCount, boys, surprise = map(int, input().split())
candy = ["candy" for i in range(houseCount)]
cryCount = 0
result = 0

for i in range(boys) :
    houseNum = int(input())
    candy[houseNum-1] = "boy"
for i in range(houseCount) :
    if cryCount == surprise :
        break
    else :
        if candy[i] == "boy" :
            cryCount += 1
        else :
            cryCount = 0
            result += 1

print(result)