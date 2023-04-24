count, types = map(int, input().split())
cards = [False] * types
check = 0

for i in range(count):
    card_number = int(input())
    if not cards[card_number-1]:
        cards[card_number-1] = True
        check += 1
    if check == types:
        print(i+1)
        break
if check < types:
    print("unlucky")