"""
1   좌표 x, y 반경, r1, r2 입력 
    1의 반경은 안전 지대 2와 1의 반경은 태풍위험지역
2   r2가 r1보다는 커야함
3   좌표를 입력할 함수 작성
4   결과는 yes or no
"""

while True:
    x, y, r1, r2 = map(int, input().split())
    if x < -100 or x > 100 or y < -100 or y > 100 or r1 <  1 or r1 > r2 or r1 > 100 or r2 > 100 :
        continue
    else :
        break
while True :
    count = int(input())
    if count < 1 or count > 100 :
        continue
    else :
        break
    
x_location = [0 for i in range(count) ]
y_location = [0 for i in range(count) ]
result = ["" for i in range(count)]
for i in range(count) :
    x_location[i], y_location[i] = map(int, input().split())
    if x_location[i] < -100 or y_location[i] < -100 or x_location[i] >100 or y_location[i] > 100 :
        continue
    else :
        if (x_location[i]-x)**2 + (y_location[i]-y)**2 >= r1**2 and (x_location[i]-x)**2 + (y_location[i]-y)**2 <= r2**2 :
            result[i] = "yes"
        else :
            result[i] = "no"
for i in range(count) :
    print(result[i])