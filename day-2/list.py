# list : 여러값을 순서대로 저장(변경 O)
list1=[1,2,3,4]
print(list1)
print(list1[2])
list1[3] = 500 #값 변경 O
print(list1)

mix_list = [1, "안녕", 10.3]
print(mix_list) #타입 혼합 시에도 O

#list 안에 list
list2 = [100, 200, ["안녕", 200], 300]
print(list2)