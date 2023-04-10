
n = int(input())


while True:
    if n / 10 < 1 and n / 10 > 0:
        print(str(n).zfill(3))
        break
    elif n / 10 >= 1 :
        print(str(n).zfill(3))
        break
    elif n == 100:
        print(n)
        break;
    else:
        n = int(input())
        