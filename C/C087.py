number = input()
if len(number) == 1 or number == number[::-1] :
    print(number)
else :
    while True :
        temp = int(number[::-1])
        number = str(int(number) + temp)
        if number == number[::-1] :
            print(number)
            break
        elif len(number) > 9 :
            break