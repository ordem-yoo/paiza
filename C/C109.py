count = int(input())
user = []
numbers = []
catch_number = ""

for i in range(count) :
    user.append(list(input()))

for j in range(count) :
    for i in range(len(user[j])) :
        if user[j][i].isdigit() == True :
            catch_number += str(user[j][i])
    numbers.append(catch_number)
    catch_number = ""

for j in range(count) :
    for i in range(j, count) :
        if int(numbers[j]) > int(numbers[i]) :
            temp = numbers[j]
            numbers[j] = numbers[i]
            numbers[i] = temp
            catch_number = user[j]
            user[j] = user[i]
            user[i] = catch_number

for i in range(count) :
    print(''.join(user[i]))