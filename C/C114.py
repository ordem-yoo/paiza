# 끝말잇기
# 처음으로 틀린 부분을 찾는 프로그램
# 대문자 소문자 틀려도 찾음

def check_error(i) : 
    if words[i][-1] != words[i+1][0] :
        error_point[i] = words[i][-1]+words[i+1][0]

while True :
    times = int(input())
    if times < 1 or times > 1000 :
        continue
    else : 
        break
    
words= [ "" for i in range(times) ]
error_point = ["" for i in range(times)]

for i in range(times) :
    while True :
        words[i] = input()
        if len(words[i]) < 1 or len(words[i]) > 50 :
            continue
        else : 
            break

for i in range(times-1) :
    check_error(i)

for i in range(times) :
    if error_point[i] != "" :
        print(error_point[i][0], error_point[i][-1])
        break
    elif i == times-1 and error_point[-1] == "" :
        print("Yes")
        break