while True:
    n = int(input())
    if n<=2 or n>=100:
        continue
    else:
        break

ball = []
for i in range(n):
    ball.append(int(input()))

while True:
    m = int(input())
    if m >= 1000 or m <= 1:
        continue
    else: 
        break
    
for i in range(m):
    a,b,cnt = map(int, input().split())
        
    if ball[a-1] >= cnt:
        ball[a-1]-=cnt
        ball[b-1] += cnt
    else :
        ball[b-1] += ball[a-1]
        ball[a-1] = 0
        
   
for i in range(n):
    print(ball[i])