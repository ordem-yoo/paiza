n = int(input())
ball = []
for i in range(n):
    ball.append(int(input()))

m = int(input())
pass_ball = []
for i in range(m):
    pass_ball.append(list(map(int, input().split())))

for i in range(m):
    current_user = pass_ball[i][0]-1
    pass_user = pass_ball[i][1]-1
    pass_count = pass_ball[i][2]
    if ball[current_user] >= pass_count:
        ball[current_user] -= pass_count
        ball[pass_user] += pass_count
    else:
        ball[pass_user] +=  ball[current_user]
        ball[current_user] = 0

for i in range(len(ball)):
    print(ball[i])