# 주민번호를 입력
# 1 또는 3이면 남자
# 아니면 (2 또는 4면) 여자

jumin = input("주민번호를 입력하세요. : ")

gender = jumin[7]

if gender == '1' or gender == '3':
    print("남자")
else:
    print("여자")