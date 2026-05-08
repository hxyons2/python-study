# 문자열
s = "Hello python"
print(s[6]) #인덱싱
print(s[6:12]) #슬라이싱

jumin="080322-4111111"
print("성별: "+jumin[7])
print("월: "+jumin[2:4])
print("일: "+jumin[4:6])
print("주민번호 뒷자리: "+jumin[7:])
print("주민번호 뒷자리: "+jumin[-7:])

s1="나는 학생입니다."
s2="파이썬을 배웁니다."
s3='재미있습니다' 
s4=""" #여러문자열을 저장할 때, 입력한 그대로 저장
    나는 학생입니다.
    나는 파이썬을 배웁니다.
    재미있습니다.
"""
print(s4)

year="66"
month="04"
day="26"
date=year+"-"+month+"-"+day
print(date)

date2 = date.split('-')
print(date2)
print(type(date2))
print(date[1][0:2], end="*")

name="kakao taxi"
name2=name.replace("k", "t", 1)
print(name2)

print("python"*5) #반복

# 문자열에서 컴마 제거
won = '63, 120, 450'
won2 = won.replace(',', '')
print(won2)

won3 = 345908800
won4 = format(won3, ',d')
print(won4)

# 문자열 대소문자, 길이
p = "python is Amazing"
print(p.lower()) # 소문자
print(p.upper()) # 대문자
print(p.capitalize()) # 첫 글자 대문자
print(p[0].isupper()) # 첫 글자 대문자인지
print(len(p)) # 문자열 길이
print(p.count("i")) # i가 몇 개 있는지

# 위치
index = p.index("i") #7
print(index)
index = p.index("i", index+1) # 14
print(index)

# 문자열 연결
words = ["python","is","easy"]
result = " ".join(words) #" " -> 리스트의 요소들을 공백으로 연결
print(result)

# 제거
text = "  Hello      Python****"
print(text.strip()) # 양쪽 공백 제거
print(text.rstrip()) # 오른쪽 공백 제거
print(text.lstrip()) # 왼쪽 공백 제거

# 자리수만큼 0으로 채우기
num = "5"
result = num.zfill(3) # 3자리수로 만들고 빈자리는 0으로 채움
print(result)

# format
age = 19
print("나는 %d살입니다."%age) # 19를 %d 자리에 넣음
print("나는 {}살 입니다.".format(age))

like = " 노래부르기"
print("나는 %d살이고 %s를 좋아해요" %(age, like))
print("나는 {0}살이고 {1}를 좋아해요".format(age, like))

print("나의 주소는 {addr}이며 , 나의 키는 {height}cm 입니다"
      .format(addr= "인천",height = 165))

# 이스케이프(탈출) 문자
print("\n배우는 과목은\n \"파이썬\"입니다.")

# \r : 커서를 맨앞으로 이동
print(" red apple\rpine") #\r은 맨앞으로
print("i like you!\b!!") # \b은 한 글자 삭제
print(" red\t apple")  # \t는 탭이동

p = "Python is Amazing"
# 인덱스 찾기
print(p.find("A")) # 왼쪽부터 찾아서 인덱스 번호 출력 , 10
print(p.rfind("A")) # 오른쪽부터 찾아서 인덱스 번호 출력 , 10
print(p.index("a") ) # 왼쪽부터 찾아서 인덱스 번호 출력 , 14
print(p.rindex("a")) # 오른쪽부터 찾아서 인덱스 번호 출력

print(p.find("java")) # 찾는 문자열이 없으면 -1 출력
# print(p.index("java")) # 없는 문자를 찾으면 에러발생

arr_Str = input('Input String :').split('-')
arr_Len = int(input('Input Number : '))
arr_Val = list(range(0, arr_Len,2))
arr_Val.remove(4)
print(arr_Str[1].find('i')+arr_Val[2])
# technology 에서 i 찾음 -> find 할때 없으면 -1
# -1 + arr_Val[2] -> -1 + 6 = 5



st = input("영어 한글자 입력..>>")

if st.isupper(): # 대문자 -> true 아니면 -> false
    print(st.lower()) # true 일때 수행 -> 소문자로 변경
else:
    print(st.upper()) # false 일때 수행 -> 대문자로 변경