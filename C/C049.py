n = int(input())
floor = []

for i in range(n):
    num = input()
    if num.isdigit():
           floor.append(int(num))
    else:        
        for i in range(len(floor)):
            floor[i] = int(floor[i])
        
overall = floor[0]    
for i in range(len(floor)-1):    
    if floor[i+1] > floor[i]:
        overall = overall + floor[i+1] - floor[i]
    elif floor[i+1] < floor[i]:
        overall = overall + floor[i] - floor[i+1]
print(overall-1)
