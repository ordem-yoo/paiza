h,m = input().split(":")

hour = 16+int(h)
if hour >24:
    result = hour -24
else:
    result = hour
    
print(f'{result}:{m}')

