# input : 키보드로부터 입력("출력문자")
# input : 문자로 기본적으로 입력받음
# 정수로 입력 하고자 할 시 앞에 int 붙임

  
# 간단한 실습
n = "apple"
print("i like", n)
print("i like"+ n)
print(3+5)
# print에서 ,는 구분 & 공뱍 +는 문자일 때 연결
#                         +는 숫자일 때 더하기
print("결과는 "+20) #오류
# +는 문자끼리, 숫자끼리 가능


# input 실습
a = int(input("첫 번째 숫자를 입력하세요. : "))
b = int(input("두 번째 숫자를 입력하세요. : "))
sum = a + b
print(sum)
 
name = input("이름을 입력하세요. : ")
print(name)

