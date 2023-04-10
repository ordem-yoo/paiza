numbers=[]
bigtemp, smalltemp = 0, 0

for i in range(5):
    numbers.append(int(input()))

smalltemp = numbers[0]

for i in range(5):
    if numbers[i] >= bigtemp:
        bigtemp = numbers[i]
    
    if numbers[i] < smalltemp:
        smalltemp = numbers[i]
        
print(bigtemp)
print(smalltemp)
    

