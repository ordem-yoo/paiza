text = input()
count = 0
for i in range(len(text)):
    if text[i] == "A":
        count = count + 1

print(count)