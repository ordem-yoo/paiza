# 가로, 세로 입력
# 각 판에 o, x 입력
# 각 판의 점수 입력
# 결과 출력

row, column = map(int, input().split())
board = []
score= []
total_score = 0

for i in range(row) :
    board.append(list(input()))
for i in range(row) :
    score.append(list(map(int,input().split())))  

for j in range(row) :
    for i in range(column) :
        if board[j][i] == "o" :
            total_score += score[j][i]

print(total_score)