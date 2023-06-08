# 파이썬의 숫자 처리 함수를 알아보자~

print(abs(-5)) # abs는 절댓값 함수
print(pow(4,2)) # 4^2
print(max(5, 12, 27)) # 최댓값 찾아서 반환해줌
print(min(5, 12, 27)) # 최솟값 찾아서 반환해줌
print(round(3.14)) # 반올림 함수

from math import * #파이썬에서 제공하는 math 라이브러리를 모두(*) 이용하겠다
print(floor(4.99)) #내림 => 4
print(ceil(3.14)) #올림 => 4
print(int(sqrt(16))) #제곱근 => 4 (걍 sqrt(16)만 하면 4.0 나오길래 내가 걍 int()씌움 ㅎ)


# 랜덤함수

from random import * #파이썬에서 제공하는 random 라이브러리를 모두(*) 이용하겠다
print(random()) # 0.0 이상 ~ 1.0 미만 임의의 값 랜덤 생성
print(random() * 10) # 0.0 이상 ~ 10.0 미만 "
print(int(random() * 10)) # 0~10 미만 임의 정수값
print(int(random() * 10) + 1) # 1~10 이하 임의 정수값
print(int(random() * 45) + 1) # 1~45 이하 임의 정수값

print(randrange(1,45)) # 1~45 미만의 임의 정수값
print(randrange(1,46)) # 1~45 이하(46 미만)의 임의 정수값
print(randint(1,45)) # 1~45 이하의 정수값 (1,45 양 끝 다 포함)

print("오프라인 스터디 모임은 매월 " + str(randint(4,28)) +"일입니다.")
