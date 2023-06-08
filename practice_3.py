#여러 줄 출력
sentence = """
여러 줄로
코딩을 해보자
"""
print(sentence) #총 4줄
sentence2 = """여러 줄로
코딩을 해보자""" #총 2줄
print(sentence2)
sentence3 = """여러 줄로
코딩을 해보자
"""
print(sentence3) #총 3줄


#슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("출생년도 : " + jumin[0:2]) # 0번째부터 2번째  직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음 ~ 6 직전
print("뒤 7자리 : " + jumin[7:]) # [7] ~ 끝까지
print("뒤 7자리 : " + jumin[-7:]) # [-7] ~ 끝까지


#문자열 처리 함수
python = "Python Is Amazing"
print(python.lower()) #다 소문자로
print(python.upper()) #다 대문자로
print(python[0].isupper()) # python[0]이 대문자냐? 묻는 것
print(len(python))
print(python.replace("Python", "Java")) #python에서 "Python"을 찾아서 "Java"로 바꿈

index = python.index("n") # n 처음 나오는 곳 어디냐
print(index)
index = python.index("n", index + 1) # index+1 위치부터 시작해서 n 어딨나 찾아라
print(index)

print(python.find("Java")) # 찾는 거 없으면 -1
# print(python.index("Java")) => 찾는 거 없으면 오류
print(python.count("n")) # n 몇 개 있나 세줌