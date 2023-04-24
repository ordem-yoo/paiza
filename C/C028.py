count = int(input())
score = 0
for j in range(count) :
    answer = list(input().split())
    if len(answer[0]) == len(answer[1]) :
        if answer[0] == answer[1] :
            score += 2
        else :
            check = 0
            for j in range(len(answer[0])) :
                if answer[0][j] != answer[1][j]:
                    check += 1
            if check == 1 :
                score += 1
print(score)