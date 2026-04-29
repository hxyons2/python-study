# 돈 입력받기
money = int(input("투입한 돈: "))
price = int(input("물건값: "))

# 거스름돈 계산
change = money - price

# 500원 개수 (몫 사용)
coin500 = change // 500
change = change % 500

# 100원 개수 (몫 사용)
coin100 = change // 100
change = change % 100

# 출력
print("거스름돈:", money - price)
print("500원 동전의 개수:", coin500)
print("100원 동전의 개수:", coin100)