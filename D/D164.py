day = int(input())

while True:
    if day / 2 == 1:
        print("OK")
        break
    elif day%2 == 0:
        day = day /2 
    else: 
        print("NG")
        break