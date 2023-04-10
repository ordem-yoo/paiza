
count = int(input())

col_address = [[0 for j in range(4)] for i in range(count)]
col_res = [[0 for j in range(4)] for i in range(count)]

for i in range(count):
    col_address[i] = input().split('.')
     
    if len(col_address[i]) == 4 and col_address[i][-1] != '':
         for j in range(4):
            if col_address[i][j].isdigit() and int(col_address[i][j]) >= 0 and int(col_address[i][j]) < 256 :
                col_res[i][j] = True
            else:
                col_res[i][j] = False
                
    else:
        col_res[i][0] = False

check_res = [True] * count

for i in range(count):
    for j in range(4):
         if col_res[i][j] == False :
            check_res[i] = False
            break
    print(check_res[i])
                        

    
