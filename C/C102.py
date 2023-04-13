calender = ["x" for i in range(31)]
band_A = ["x" for i in range(31)]
band_B = ["x" for i in range(31)]
count = 0

def band_compare(date) :
    global count
    if count % 2 == 0 :
        calender[date] = "A"
        count += 1
    else :
        calender[date] = "B"
        count += 1
    
while True:
    band_A_count = int(input())
    if band_A_count < 1 or band_A_count > 31:
        continue
    else :
        break
    
for i in range(band_A_count):
    date = int(input())
    band_A[date-1] = "A"

while True:
    band_B_count = int(input())
    if band_B_count < 1 or band_B_count > 31:
        continue
    else :
        break 
    
for i in range(band_B_count):
    date = int(input())
    band_B[date-1] = "B"

for i in range(31):
    if band_A[i] != "x" and band_B[i] != "x":
        band_compare(i)
    elif band_A[i] != "x" and band_B[i] == "x":
        calender[i] = "A"
    elif band_A[i] == "x" and band_B[i] != "x":
        calender[i] = "B"
    else:
        calender[i] = "x"
    print(calender[i])
