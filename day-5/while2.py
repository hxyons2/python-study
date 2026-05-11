# 숫자 입력  -> 출력 반복, 0을 입력하면 종료

a=True
while a: #True(참) 반복, (False)거짓이면 탈출
    num = int(input("숫자를 입력하세요: "))
    if num == 0:
        a = False
print("반복문 종료")

print("="*20)

menu= ["쫄면", "김밥", "냉면", "오뎅"]
b=input("메뉴 선택 : ")
while b in menu: #(b가 menu에 없으면 반복문 탈출) 조건이 참일 때 수행 #in은 포함 연산자
    print(b)
    b=input("메뉴 선택 : ")
    #while 문장 안에서 반드시 거짓으로 변경되는 문장이 나와야 함

