a = int(input())

while True:    
    if a <= 20 and a>=1:
        m=a**2 * 6
        break
    else:
        a = int(input())
        
print(m)