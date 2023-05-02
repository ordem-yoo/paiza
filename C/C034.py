# a + b = c 또는 a - b = c를 생성
# a, b, c 중 하나를 비운다 빈 자리가 답이 되어야 한다
# 0 2 4

def calculate() :
    if expression[1] == "-" and expression[2] != "x":
        expression[2] *= -1
        
    if expression[0] == "x" :
        return expression[4] - expression[2]
    elif expression[2] == "x" :
        return abs(expression[4] - expression[0])
    elif expression[4] == "x" :
        return expression[0] + expression[2]
    else :
        return None
expression = list(input().split())
for i in range(0, len(expression), 2) :
    if expression[i] != "x" :
        expression[i] = int(expression[i])
        
print(calculate())