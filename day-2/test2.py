# 가격 변수 (미리 정해진 값)
americano_price = 2000
latte_price = 3000
cappuccino_price = 3500

# 판매 개수 입력받기
americano_count = int(input("아메리카노 판매 개수: "))
latte_count = int(input("카페라떼 판매 개수: "))
cappuccino_count = int(input("카푸치노 판매 개수: "))

# 매출 계산
total = (americano_price * americano_count) + \
        (latte_price * latte_count) + \
        (cappuccino_price * cappuccino_count)

# 결과 출력
print("총 매출은", total, "원입니다.")