# 식품 m kg 구매
# p %를 판매
# (100-p) 에서 q% 판매
# 남은 값은 

m, p, q = map(int,input().split())

notsell = (m/100)*(100-p)
notsellfood = (notsell/100)*(100-q)
print(notsellfood)