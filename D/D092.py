x,y,p = map(int,input().split())
a,b,m = map(int,input().split())

seat1 = p/(x*y)
seat2 = m/(a*b)

if seat1 < seat2:
    print(x,y,p)
elif seat1 > seat2:
    print(a,b,m)
else:
    print("DRAW")

