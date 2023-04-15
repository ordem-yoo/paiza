import sys
sys.setrecursionlimit(10**7)

def factorial (num) :
    if num == 1:
        return num
    else:
        return num*factorial(num-1)

n = int(input())

print(factorial(n))