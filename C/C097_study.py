# 최소 공배수 , 최대 공약수의 특징 생각해볼 것

# 최소 공배수
"""
    10 20
    10과 20의 최소 공배수는 20
    최소 공배수가 나온 원리는 두 수를 비교하고
    큰 수의 배수에서 작은 수의 배수를 찾는 방식  
"""

a, b = map(int, input().split())
def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1): # 10 과 20 이라고 하면 max(a,b)는 20이 나오고, (a*b)+1 은 201이다. 즉, 20부터 200까지 반복
        print(i)                            # i를 a와 b로 나누었을 때 둘 다 나머지가 0이 나오는 것이다. 
        if i % a == 0 and i % b == 0:  
            return i
print(lcm(a,b))

# 최대 공약수
"""
    15 20
    15와 20의 최대 공약수는 5
    최대 공약수가 나온 원리는 두 수의 공통 약수를 찾고,
    그 중에서 가장 큰 숫자를 찾는 방식
"""
x, y = map(int, input().split())
def gcd(x,y):
    for i in range(min(x,y), 0, -1): # a와 b중 작은 숫자를 선택하고, 선택한 숫자가 0이 될 때까지 반복한다. -1씩 감소하면서
        if x % i == 0 and y % i == 0: # a와 b 둘 다 i로 나누어서 둘 다 나머지가 0이 나오는 값을 반환한다.
            return i
print(gcd(x,y))
        