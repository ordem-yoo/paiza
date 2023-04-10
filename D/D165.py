def check_password(password):
    for num in password:
        print(num)
        if password.count(num) > 1:
            return "NG"
    return "OK"

password = input()
print(check_password(password))

# for 문에서 입력받은 값을 range 위치에서 가져오면 한자리씩 가져올 수 있음
# count 메서드는 부분문자열의 개수를 세는 메서드