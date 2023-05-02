ferris, groups = map(int,input().split()) # 곤돌라 수, 일행 팀 수
overload = [int(input()) for i in range(ferris)] # 곤돌라에 탈 수 있는 제한 수
teamMember = [int(input()) for i in range(groups)] # 일행들의 인원 수
boardedPeople = [0 for i in range(ferris)] # 각 곤돌라에 탑승한 총 인원 수
rotate, count, remainder = 0, 0, 0 # 곤돌라의 번호 # 

while teamMember[groups-1] != 0 :
    if remainder == 0 : # 첫 일행, 다음 일행이 처음 탑승
        if overload[rotate] >= teamMember[count] : # 탑승 제한 인원수 보다 적을 때
            boardedPeople[rotate] = teamMember[count]
        else : # 탑승 제한 인원수 보다 많을 때
            boardedPeople[rotate] = overload[count]
            remainder = teamMember[count] - overload[rotate]
    else :  # 일행의 나머지 인원 탑승할 때
        if overload[rotate] >= remainder : # 탑승 제한 인원수 보다 적을 때
            boardedPeople[rotate] = remainder
            teamMember[count] = 0
            remainder = 0
            count += 1
            print(boardedPeople)
            print(teamMember)
        else : # 탑승 제한 인원수 보다 많을 때
            boardedPeople[rotate] = overload[rotate]
            remainder -= overload[rotate]
    rotate += 1
    if rotate > ferris :
        rotate = 0

