month, day = map(int,input().split())

while True:
    if month<= 12 and month >= 1 and day <= 31 and day >= 1:
        smonth = list(map(int,str(month)))
        sday = list(map(int,str(day)))
        
        if len(smonth) <2 and len(sday) < 2:
            if smonth[0] == sday[0]:
                print("Yes")
                break
            else:
                print("No")
                break
        elif len(smonth) < 2 and len(sday) == 2:
            if smonth[0] == sday[0] and smonth[0] == sday[1] :
                print("Yes")
                break
            else:
                print("No")
                break
        elif len(smonth) == 2 and len(sday) < 2:
            if smonth[0] == smonth[0] and smonth[1] == sday[0] :
                print("Yes")
                break
            else:
                print("No")
                break
        elif len(smonth) == 2 and len(sday) == 2:
            if smonth[0] == smonth[1] and smonth[0] == sday[0] and smonth[0] == sday[1] or smonth[0] == sday[0] and smonth[1] == sday[1]:
                print("Yes")
                break
            else:
                print("No")
                break
        else:
            print("Hello")
    else:
        month = int(input())
        day = int(input())