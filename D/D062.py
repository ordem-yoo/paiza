x,y,z = map(int, input().split())

for i in range(x):
    print(chr(65+i), end="")
    if i == x-1:
        print("")


for i in range(y):
    print(chr(65+x+i), end="")
    if i == y-1:
        print("")
   

for i in range(z):
    print(chr(65+x+y+i), end="")


# chr메서드 
# 아스키 코드를 불러올 수 있음