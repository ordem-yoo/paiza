player = int(input())
scores = list(map(int, input().split()))
medals = ['G', 'S', 'B']
rank = []

for i in range(player):
    cnt = 1
    for j in range(player):
        if scores[i] < scores[j]:
            cnt += 1
    rank.append(cnt)

for i in range(player):
    if rank[i] == 1:
        print(medals[0])
    elif rank[i] == 2:
        print(medals[1])
    elif rank[i] == 3:
        print(medals[2])
    else:
        cnt = 0
        for j in range(player):
            if rank[j] < rank[i]:
                cnt += 1
        if cnt == 1:
            print(medals[1])
        elif cnt == 2:
            print(medals[2])
        else:
            print('N')