while True :    
    person = int(input())
    if person < 1 or person > 1000 :
        continue
    else :
        break

years = [ 0 for i in range(person)]
beans = [0 for i in range(person)]
def give_bean(start, end, cnt) :
    global beans, years
    for j in range(start-1, end, 1) :
        beans[j] += cnt
        if beans[j] > years[j] :
            beans[j] = years[j]

for i in range(person):    
    years[i] = int(input())

while True:
    times = int(input())
    if times < 1 or times > 100 :
        continue
    else :
        break

for i in range(times) :
    while True :
        first, last, cnt = map(int, input().split())
        if first >= 1 and first <= last and last <= person and cnt >= 1 and cnt <= 100 :
            break
        else : 
            continue
    give_bean(first, last, cnt)

for i in range(person):
    print(beans[i])