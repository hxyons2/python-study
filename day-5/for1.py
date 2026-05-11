# a = "봄"
# b = "여름"
# print(a, b, sep="과", end="끝")
# sep : 변수 사이에 들어가는 것을 나타냄
# end : (print문이 끝난 후에 들어가는 것을 나타냄) 줄을 바꾸지 않고 옆으로 표시(공백도 가능)'

# for i in range(1, 100, 2): 1~99까지 2씩 증가하는 수열
# 구구단에서 원하는 단을 입력 받아서 출력하는 프로그램
dan = int(input("원하는 단은? : ")) 
for i in range(1, 10):
    print(dan, "*", i, "=", dan*i)

for i in range(2, 10): #2-9단
    print(i, "단")
    for j in range(1, 10): #1-9 수
        print(i, "*", j, "=", i*j, end=" ") #줄 바꿈 없이 옆으로 출력
    print() #줄 바꿈

import time
print()
for k in range(10, 0, -1): #10부터 1까지 1씩 감소하는 수열
    print(k)
    time.sleep(1) #1초마다 숫자 출력
print("발사!!")