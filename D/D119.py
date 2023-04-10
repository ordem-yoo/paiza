import math

num = int(input())
print
while True:
    if num >= 1 and num <= 15:
        if num == 15:
            result = str(round(math.pi, num))
            break
        else:
            result = str(round(math.pi, num+1))
            result = result[:-1]
            break
    else: 
        num =int(input())
print(result)

# 왜 11은 안되는걸까?
# 1  3.1
# 2  3.14
# 3  3.141
# 4  3.1415
# 5  3.14159
# 6  3.141592
# 7  3.1415926
# 8  3.14159265
# 9  3.141592653
# 10 3.1415926535
# 11 3.14159265358
# 12 3.141592653589
# 13 3.1415926535897
# 14 3.14159265358979
# 15 3.141592653589793