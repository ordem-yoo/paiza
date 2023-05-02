typeCount, packCount = map(int,input().split())
orderPack = []
randomPack = []

for i in range(packCount) :
    orderPack.append(int(input()))
for i in range(packCount) :
    randomPack.append(int(input()))

for j in range(packCount) :
    for i in range(packCount) :
        if randomPack[j] == orderPack[i] :
            orderPack[i] = 0
            break

if orderPack.count(0) != packCount :
    print("No")
else :
    print("Yes")