"""
단어 개수 입력 받아
찾을 문자열 입력 받아
저장할 문자열 입력 받아

결과로 찾을 문자열이 있는 애들을 전부 출력해
"""
while True :
    count = int(input())
    if count< 1 or count > 100 :
        continue
    else :
        break
while True :
    string = input()
    if len(string) < 1 or len(string) > 100 :
        continue
    else :
        break

words = [ "" for i in range(count) ]
none_count = 0
for i in range(count) :
    while True :
        words[i] = input()
        if len(words[i]) < 1 or len(words[i]) > 100 :
            continue
        else :
            break
        
for i in range(count) :
    if string in words[i] :
        print(words[i])
    else :
        none_count += 1
if none_count == count :
    print("None")