find = input()
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

if find in alpha:
    number=alpha.index(find)
    print(number+1)