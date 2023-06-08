##### 모듈 (필요한 것들끼리 부품처럼 만들어진 파일. 함수나 클래스 등이 담긴 파일을 모듈이라 함! 모듈의 확장자는 .py 임!)
# 모듈은 내가 그 모듈을 쓰려는 파일과 같은 경로에 있거나, 파이썬 라이브러리들이 모여 있는 폴더에 있어야 사용 가능.



### 영화관 가격 모듈을 만들어보자

# 일반 가격
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))

# 조조할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000))