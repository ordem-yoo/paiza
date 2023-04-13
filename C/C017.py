while True:
    dealer_A, dealer_B = map(int,input().split())
    if dealer_A <1 or dealer_B <1:
        continue
    else:
        break
    
count = int(input())
if count>= 40 or count<1:
    count = int(input())
else: 
    result = ["" for i in range(count)]

def discrimination(a, b) :
    if dealer_A > a  :
        result[i] = "High"
    elif dealer_A == a and dealer_B < b:
        result[i] = "High"
    elif dealer_A == a and dealer_B > b:
        result[i] = "Low"
    else: 
        result[i] = "Low"

for i in range(count):
    number_A, number_B = map(int, input().split())
    if number_A < 1 or number_A > 10 or number_B < 1 or number_B > 10 or (dealer_A == number_A and dealer_B == number_B):
        number_A, number_B = map(int, input().split())
    else:
        discrimination(number_A, number_B)

for i in range(count):
    print(result[i])
