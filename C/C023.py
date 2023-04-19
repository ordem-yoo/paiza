"""
복권

당첨번호 먼저 입력

발행할 복권 수 입력

각 복권의 번호 입력

각각 복권에서 맞은 개수 출력

당첨에서 복권들 자리가 맞는지 각각 확인

"""
win_code = list(map(int,input().split()))
while True :
    lottery_cnt = int(input())
    if lottery_cnt < 1 or lottery_cnt > 100 :
        continue
    else :
        break
    
lotterys =  [[] for i in range(lottery_cnt)]
rank_cnt = [0 for i in range(lottery_cnt)]

for i in range(lottery_cnt) :
    lotterys[i] = list(map(int,input().split()))

for k in range(6) :
    for j in range(lottery_cnt) :
        for i in range(6) :
            if win_code[k] == lotterys[j][i] :
                rank_cnt[j] += 1

for i in range(lottery_cnt) :
    print(rank_cnt[i])