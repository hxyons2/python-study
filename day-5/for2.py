# for i in range(6)
# 0 부터 5까지 1씩 증사
# 딕셔너리 : 키와 값으로 이루어져 있음
snack = {
    "새우깡" : 3000,
    "매운 새우깡" : 3000,
    "양파링" : 4000

}
for i in snack:
    print(i)
for j in snack.items(): # ()를 붙이지 않으면 items는 메서드 이기 때문에 실행되지 않음
    print(j)
# items 키랑 값 전부 출력

# 리스트
fruit = ["파인애플", "참외" , "배" , "오렌지", "골드키위"]
cart = []
for i in fruit:
    if len(i) < 3 :
        cart.append(i)
print(cart)