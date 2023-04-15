while True:
    times = int(input())
    if times < 1 or times > 10 :
        continue
    else :
        break

numbers = [ 0 for i in range(times) ]

for i in range(times) :
    numbers[i] = int(input())

numerator = numbers[-1] * numbers[-2] + 1
denominator = numbers[-1]

for i in range(3, times+1) :
    temp = denominator
    denominator = numerator
    numerator = temp 
    numerator = (denominator * numbers[-i]) + numerator

print(numerator, denominator)