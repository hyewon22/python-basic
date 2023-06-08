#문자열 포맷
#방법1
print("나는 %d월생입니다." % 1) #정수
print("%s는 귀여워" % "밤송이") #문자열
print("Bamsong은 %c로 시작해" % "B") #문자 한 개
#s는 정수든 문자 한 개든 다 받을 수 있지. 문자열로 인식할 뿐!
print("나는 %s색과 %s색을 좋아해" % ("분홍", "파란"))

#방법2
print("저는 {}년생이에요".format(2000))
print("나는 {}색과 {}색을 좋아해" .format("분홍", "파란"))
print("나는 {0}색과 {1}색을 좋아해" .format("분홍", "파란"))
print("나는 {1}색과 {0}색을 좋아해" .format("분홍", "파란"))

#방법3
print("나는 {age}살이고 {color}색을 좋아해" .format(age = 20, color ="파란"))
print("나는 {age}살이고 {color}색을 좋아해" .format(color ="파란", age = 20))

#방법4 (v3.6 이상~)
age=20
color="분홍"
print(f"나는 {age}살이고 {color}색을 좋아해")



########
#탈출문자

# \n : 줄바꿈
print("밤송이\n짱\n귀여워")

# \" \' : 문장 내에서 따옴표
print("김밤송 \"너무귀여워\"")

# \\ : 문장 내에서 \
print("C:\\Users\\fear_\\Desktop\\Python Workspace")

# \r : 커서 맨 앞으로 이동
print("Red apple\rPine") # => Pineapple 출력

# 그 외에도 백스페이스는 \b , 탭은 \t




####퀴즈
juso = "http://naver.com"
nya = juso[7:-4]
print(nya)
print(nya[:3])
le = len(nya)
print(le)
cnt = nya.count("e")
print(cnt)
print(nya[:3] + str(le) + str(cnt) + "!")