###퀴즈
from random import *
lili= [1,2,3,4,5]
shuffle(lili)
print(lili)
print(sample(lili, 1)) # sample(O,X)는 O에서 X개만큼 샘플 랜덤으로 뽑는 거.

lst = list(range(1,21)) # 1 ~ 21-1까지 리스트 함수로 리스트 생성.
shuffle(lst)
print(lst)
print("치킨 : " + str(lst.pop()))
print("커피 : " + str(sample(lst,3)))



######
# if문 (조건문)

weather = input("오늘 날씨 어때? ") # 터미널에 오늘 날씨 어때? 뒤에 커서 뜨고 거기 입력하면 됨. input()은 항상 문자열만 받는 입력함수.
if weather == "비" or weather == "눈" :
    print("우산 챙겨라")
elif weather == "미세먼지" :
    print("마스크 챙겨라")
else :
    print("준비물 없다")


temp = int(input("기온은 어때? ")) # input()은 입력된 게 문자열로만 인식되니 int()로 감싸주기
if temp >= 30 :
    print("나가지 마 너무 더워")
elif temp >= 10 and temp < 30 :
    print("괜찮은 날씨야")
elif 0 <= temp < 10 : 
    print("쌀쌀해")
else :
    print("추워잉")



#####
# for문 (반복문)

for waiting in range(1,5): #1 ~ 5-1까지
    print("대기번호 : {}".format(waiting))

starbucks = ["밤송", "공주", "송이"]
for customer in starbucks:
    print("{0}, 커피 나왔습니다".format(customer))


####
# while문 (반복문)
sonnim = "헤지"
index = 5
while index >= 1 :
    print("{0} 님, 커피 나왔습니다. {1}번 남았습니다.".format(sonnim, index))
    index -= 1
    if index == 0 :
        print("{} 님, 커피는 버릴게요.".format(sonnim))

son = "송밤"
person = "Unknown"
while person != son : # person과 son이 다를 때 반복됨
    print("{}, 커피 나왔어요.".format(son))
    person = input("이름이 어떻게 되세요? ")
    if person == son :
        print("{}, 맛있게 먹어요!".format(person))


#########
# continue와 break

absent = [2,5]
nobook = [7]
for student in range(1,11) :
    if student in absent :
        continue
    if student in nobook : # 리스트에만 in 쓸 수 있음
        print("{}번, 교무실로!".format(student))
        break
    print("{}번, 책 읽어~".format(student))


####### 한 줄 for
# 출석번호 1,2,3,4인데 100붙여서 101, 102, 103, 104로 바뀜.
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students] # students 리스트 항목들을 하나씩 i에 담고 i+100을 다시 students 리스트로 반환
print(students)

# 글자수 리스트로 반환
hero = ["밤송", "송이공주", "밤밤밤밤밤"]
print(hero)
hero = [len(i) for i in hero] # hero리스트 속 항목들 글자수 길이를 다시 hero리스트에 저장
print(hero)

# 이름들 대문자로 변환
prince = ["Bamsong", "song", "baM"]
prince = [i.upper() for i in prince]
print(prince)




#######퀴즈
from random import *
cnt = 0
for num in range(1, 51) :
    time = randrange(5,51)
    if 5 < time < 15 :
        print("[O] {}번째 손님 : 소요시간 {}분".format(num, time))
        cnt += 1
    else :
        print("[] {}번째 손님 : 소요시간 {}분".format(num, time))
print("\n총 손님 수 : " + str(cnt))
#계속 돌아가면서 다시 초기화되려면 for문 안에 time=randrange(5,51)가 있어야 하는구나... 배웠다!!! 그리고 sample(list,1) 이건 5 < sample(list,1) < 15가 안되네.