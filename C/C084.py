text = input()

for i in range(int(len(text))+2):
    print("+", end="")
print("")
print(f"+{text}+")
for i in range(int(len(text))+2):
    print("+", end="")