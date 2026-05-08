st = input("영어 한 글자를 입력하세요. : ")

if st.isupper(): # 대문자 -> true 아니면 -> false
    print(st.lower()) # true 일때 수행 -> 소문자로 변경
else:
    print(st.upper()) # false 일때 수행 -> 대문자로 변경



# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
# 사용자로부터 score를 입력받아 학점을 출력하라.
# 점수      학점
# 81~100    A
# 61~80     B
# 41~60     C
# 21~40     D
# 0 ~ 20    E

score = int(input("점수를 입력하세요. : "))

# if score >= 81 and score <= 100:
#    print("A")
# elif score >= 61 and score <= 80:
#    print("B")
# elif score >= 41 and score <= 60:
#     print("C")
# elif score >= 21 and score <= 40:
#     print("D")
# else:
#     print("E")

num = jumin.split("-")[1] # ["123456", "1234567"]
if num[0] == '1' or num[0] == '3': 
    # num[1][0]
# (jumin[7] == '1' or jumin[7] == '3'):
#     print("남자")
else:
    print("여자")



# 사용자로부터 세 개의 숫자를 입력 받은 후
# 가장 큰 숫자를 출력하라
num1 = int(input("첫 번째 숫자를 입력하세요. : "))
num2 = int(input("두 번째 숫자를 입력하세요. : "))
num3 = int(input("세 번째 숫자를 입력하세요. : "))
if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2) 
else:    
    print(num3)    