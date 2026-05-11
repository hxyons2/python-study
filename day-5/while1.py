# 1~100까지 합과 개수
sum = 0
cnt = 0

while cnt < 101: #1~100 만족할 때까지 반복
    sum = sum+cnt # 합을 누적
    cnt = cnt+1 # 개수를 1씩 증가
print("개수는: ", cnt)
print("합계는: ", sum)
#초기값
#while 조건
#   증감