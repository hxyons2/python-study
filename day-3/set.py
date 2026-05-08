# set(집합)
# 순서가 없음, 중복 안 됨
# {}, set([])

my_set={"홍길동", "김길동", "장길동"}
print(my_set)

football={"홍길동", "김길동", "장길동"}
# baseball={"홍길동", "오길동", "김하성"}
baseball=set(["홍길동", "오길동", "김하성"])

# 교집합
print(football & baseball)
print(football.intersection(baseball))

# 합집합
print(football | baseball)
print(football.union(baseball))

# 차집합
print(football - baseball)
print(football.difference(baseball))

# 추가
football.add("김길동") #중복 안 됨. 대신 오류로 뜨진 않음.
print(football)

# 삭제
baseball.remove("오길동")
print(football)

print(type(baseball))

spo1=list(baseball)
print(type(spo1))

spo2=tuple(baseball)
print(type(spo2))