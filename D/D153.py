x,y,z= map(int, input().split())

if x >= y and x >= z :
    if y >= z:
        print(y)
    else: 
        print(z)
elif y>= x and y >= z :
    if x >= z:
        print(x)
    else: 
        print(z)
elif z >= x and z >= y:
    if x >= y:
        print(x)
    else: 
        print(y)