weight, mandarinCount = map(int,input().split())
mandarin = []
for i in range(mandarinCount) :
    mandarin.append(int(input()))
    if mandarin[i] < weight :
        mandarin[i] = weight
    if mandarin[i] % weight >= round(weight/2) :
        mandarin[i] = weight * round(mandarin[i]/weight)
    else :
        mandarin[i] = (mandarin[i]//weight) * weight

for i in range(mandarinCount) :
    print(mandarin[i])