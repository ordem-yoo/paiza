# 인턴십 1 ~ 3
# 200엔 교통비

# 인턴십 4~6
# 호텔 숙박 1박당 300엔
# 신칸센 왕복 400

# 인턴십 8 ~ 10
# 2박 600엔
# 신칸센 400엔

# 귀가 
# 교통비 200엔

# 신칸센 편도, 숙박비, 인턴십 횟수 입력
# 인턴십 횟수만큼 인턴십 일자 입력

shinkansen, hotel, internship = map(int, input().split())
internshipLog = [[] for i in range(internship)]
cost = shinkansen

for i in range(internship) :
    internshipLog[i] = list(map(int,input().split()))
    
for i in range(internship-1):
    date = internshipLog[i+1][0] - internshipLog[i][1]
    shinkansenCost = shinkansen * 2
    hotelCost = date * hotel
    if shinkansenCost <= hotelCost :
        cost += shinkansenCost
    else :
        cost += hotelCost
cost += shinkansen
print(cost)
        