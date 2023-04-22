"""
상자 수 n 공 반지름 r

상자 수 만큼 가로 세로 높이 입력

들어갈 수 있는 상자의 인덱스만 출력

"""

while True :
    boxnum, radius = map(int, input().split())
    if boxnum < 1 or boxnum > 100 or radius < 1 or radius > 100 :
        continue
    else : 
        break
    
boxlength = [ [] for i in range(boxnum)]
results = []

for i in range(boxnum) :
    boxlength[i] = list(map(int, input().split()))

for j in range(boxnum) :
    for i in range(3) :
        if radius * 2 <= boxlength[j][i] :
            if i == 2 :
                results.append(j+1)
        else :
            break

for i in range(len(results)) :
    print(results[i])
    
# n, r = map(int, input().split())  # 상자의 수 n과 볼의 반경 r을 입력받음
# for i in range(1, n + 1):  # 각 상자에 대해 반복
#     h, w, d = map(int, input().split())  # 상자의 높이, 폭, 깊이를 입력받음
#     if min(h, w, d) >= 2 * r:  # 볼의 직경보다 모든 면의 최소 길이가 크거나 같으면
#         print(i)  # 상자 번호를 출력함