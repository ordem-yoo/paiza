t, m = map(int, input().split())
result="No"

def checking(t, m) :
    if t >= 25 and m <= 40:
        result = "No"
    elif t >= 25 or m <= 40:
        result = "Yes"
    else:
        result ="No"
        
    return result

while True:
    if t <= 40 and t >= 0 and m <= 100 and m >= 0:
        print(checking(t, m))        
        break
    else:
        t, m = map(int, input().split())


