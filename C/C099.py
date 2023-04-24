count, length = map(int, input().split())
minus = 0
for i in range(count-1) :
    n = int(input())
    minus += n
print(length*(length*count-minus))