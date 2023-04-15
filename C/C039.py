plus_count, units, tens, hundreds= 0, 0, 0, 0
 
while True:
    code = input()
    if len(code) <3 or len(code) > 100 :
        continue
    else :
        break

for i in range(len(code)) :
    if code[i] == "+" :
        plus_count += 1

calculate_field = [ "" for i in range(plus_count) ]
calculate_field = code.split("+")

for j in range(len(calculate_field)) : 
    for i in range(len(calculate_field[j])) :
        if calculate_field[j][i] == "<" :
            tens += 1
        elif calculate_field[j][i] == "/" :
            units += 1

if units / 10 > 1 :
    tens += int(units / 10 )
    units  %= 10 
if tens / 10 > 1 : 
    hundreds += int(tens / 10)
    tens %= 10
result = (hundreds * 100) + (tens * 10) + units
print(result)