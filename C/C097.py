
n, x, y = map(int, input().split())
price = [" " for i in range(n)]

def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1): 
        print(i)
        if i % a == 0 and i % b == 0:
            
            return i
        
maxNum = lcm(x,y)


for i in range(n):
    price[i]= "N"

for i in range(int(n/x)):
    price[(i*x)+x-1] = "A"

for i in range(int(n/y)):
    price[(i*y)+y-1] = "B"

for i in range(int(n/maxNum)):
    price[(i*maxNum)+maxNum-1] = "AB"
    
for i in range(n):
    print(price[i])


'''
a, b 두 개의 선물 종류
// 당첨 조건
정수 x의 배수번째 == A상품 - A 상품 당첨자는 A로 표시
정수 y의 배수번째 == B상품 - B 상품 당첨자는 B로 표시
xy의 배수는 AB 상품 - AB 표시
둘 다 해당 안돼면 N으로 표시

'''
