while True :
    flower_count = int(input())
    if flower_count < 1 or flower_count > 1000 :
        continue
    else :
        break
while True :
    flower_array = list(input())
    check_flower_array = list(input())
    if len(flower_array) != flower_count or len(flower_array) != flower_count :
        continue
    else :
        break
    
result = []
for i in range(flower_count) :
    check_flower_array.insert(0,check_flower_array[-1])
    check_flower_array.pop(-1)
    if check_flower_array == flower_array :
        result.append("Yes")
    else :
        result.append("No")
if "Yes" in result :
    print("Yes")
else :
    print("No")