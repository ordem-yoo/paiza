number = [24,6,8,10,12,14,16,18,20,22]
distance = 0

while True:
    first, second, third = map(str, input().split("-"))
    if len(first)== 4 and len(second) == 2 and len(third) == 4 :
        break
    elif len(first)== 3 and len(second) == 4 and len(third) == 4 :
        break
    else :
        continue

length = len(first)+len(second)+len(third)

for i in range(len(first)):
    distance += number[int(first[i])]
for i in range(len(second)):
    distance += number[int(second[i])]
for i in range(len(third)):
    distance += number[int(third[i])]

print(distance)