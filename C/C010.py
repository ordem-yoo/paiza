

while True:
    a, b, r = map(int, input().split())
    if a <= 100 and a >= 0 and b <= 100 and b >= 0 and r <= 100 and r >= 1:
        break
    else:
        a, b, r = map(int, input().split())

while True:
    n = int(input())
    if n <= 1000 and n >= 1:
        break
    else:
        n = int(input())

result = ["" for i in range(n)]

for i in range(n):
    x, y = map(int, input().split())
    while True:
        if x <= 100 and x >= 0 and y <= 100 and y >= 0 :
            break
        else:
            x, y = map(int, input().split())

    distance = (x-a)**2+(y-b)**2
    
    if distance < r**2 :
        result[i] = "noisy"
    else:
        result[i] = "silent"

for i in range(n):
    print(result[i])