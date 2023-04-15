n = int(input())
ball = [0 for x in range(n)]

def moveBall(a, b, c):
    ball[a-1] = ball[a-1] - c
    ball[b-1] = ball[b-1] + c
    if ball[a-1] < 0:
        ball[b-1] = ball[b-1]+ball[a-1]
        ball[a-1] = 0
        
for i in range(n):
    ball[i] = int(input())

m = int(input())
for j in range(m):
    a,b,c = map(int, input().split())
    moveBall(a,b,c)

for k in range(n):
    print(ball[k])