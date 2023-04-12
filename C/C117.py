

n,m = map(int, input().split())
a,b,c = map(int,input().split())
ramen = [0 for i in range(n)]
count = 0

for i in range(n):
    ramen[i] = int(input())
for i in range(n):
    ramen[i] = ((c*ramen[i])-a)-(b*m)

for i in range(n):    
    if ramen[i] < 0:
        count = count+1
                
print(count)
