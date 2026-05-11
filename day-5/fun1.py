# 함수
def add(a, b): # a, b는 매개변수
    return a + b

a, b = map(int, input("두 수 입력: ").split())
sum = add(a, b)
print(sum)

# sum() : 합계
# len() : 길이
# 숫자 리스트의 평균을 반환
# 1. 리스트의 합계를 구한다. (sum() 함수 활용 가능)
# 2. 리스트의 개수를 구한다 (len() 함수 활용 가능)
# 3. 합계를 개수로 나눈 값을 return 한다
def avg(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

score_list = [80, 90, 100, 50, 70]
average = avg(score_list)
print(f"평균: {average}")