hundreds, units =map(int, input().split())
result = []

for j in range(1,10) :
    for i in range(10) :
        if (10 * j + i) * i == hundreds * 100 + 10 * j + units :
            result.append([j,i])

if len(result) == 0 :
    print("No")
else :
    print(result[0][0],result[0][1])