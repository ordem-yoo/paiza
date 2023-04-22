# 초 N 함수의 개수 M
# 초마다 동작할 함수들을 각각 나열
# 초의 배수마다 지정한 함수 실행
# 공통배수인경우는 낮은 숫자가 먼저 쓴 숫자가 실행

seconds, functions = map(int, input().split())
functionList = []
functionNumber = []
result = []
temp = ""

def seconds_check(second) :
    global temp
    for i in range(len(functionList)) :
        if second % functionNumber[i] == 0 :
            temp += functionList[i][1] + " "
    if temp == "" :
            temp = str(second)
    print(temp.rstrip())
    temp = ""
    
for i in range(functions) :
    functionList.append(list(input().split()))
    functionNumber.append(int(functionList[i][0]))

for i in range(1,seconds+1) :
    seconds_check(i)