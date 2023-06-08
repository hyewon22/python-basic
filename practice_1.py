print(126)
print(3*(4*5))
print(6/3) # 2.0 (실수형 몫)
print(6//3) # 2 (정수형 몫)
print('파이썬')
print("최고")
print("밤송"*9)

print(3<5) #boolean => True 출력
print(not (5>3)) # 5>3은 True니 False 출력
print(not (1 != 3))
print((3>0) and (3<5)) # and 대신 & 써도 ㅇㅋ. and는 둘 다 참이어야 True고 or은 하나만 참이어도 True
print(5>4>3) #5는 4보다 크고 4는 3보다 크다 => True
print(5>4>7) #5는 4보다 크고 4는 7보다 크다 => 뒷부분이 가짜라 False
print (False)

animal = "기니피그"
name = "밤송"
age = 3
is_adult = age>=3

print("우리 집" + animal + "이름은 " + name + "입니다.")
print("나이는 " + str(age) + "살이죠.") #정수형 변수는 +있는 print문에서 사용하려면 str()로 감싸서 정수형에서 문자형으로 바꿔줘야.
print(name + "은 어른일까요? " + str(is_adult)) #boolean형 변수도 +있는 print문에서 사용하려면 str()로 감싸서 문자형으로 바꿔줘야!

print("나이는 ", age , "살이죠.") 
print(name, "은 어른일까요? ", is_adult)
#요렇게 ,로 이어줄 때는 str()로 안 감싸도 ㅇㅋ. 근데 , 쓰면 띄어쓰기가 한 칸씩 무조건 포함이 됨!

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")