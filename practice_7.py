# 함수 정의
def open_acount() :
    print("계좌가 개설되었습니다.")

# 함수 호출
open_acount()


# 함수 예시
def deposit(balance, money) : #입금
    print("입금 완료. 잔액은 {}원입니다.".format(balance+money))
    return balance+money

balance = 0 #잔액
balance = deposit(balance, 1000) # 여기서 입금완료. 잔액은 1000원입니다.출력되고 1000원이 balance에 저장됨.
print(balance) # deposit()에서 return값으로 balance+money 해줬으니 balance+money 반환됨. 여기서 저장된 1000원 출력되는 것.


def withdraw(balance, money) : #출금
    if balance >= money :
        print("출금 완료. 잔액은 {}원.".format(balance - money))
        return balance - money
    else :
        print("출금 실패. 잔액은 {}원.".format(balance))
        return balance

balance = withdraw(balance, 500)


def withdraw_night(balance, money) : #저녁 출금
    susuryo = 100 # 수수료 100원
    return susuryo, balance-money-susuryo # 요렇게 여러 개의 값을 한 번에도 반환 가능

susuryo, balance = withdraw_night(balance, 500)
print("수수료 {0}원이고, 잔액은 {1}원.".format(susuryo, balance))



# 함수 기본값 설정
def profile(name, age=20, mainlang="파이썬") : # 함수 호출되고 값 전달받을 때 age랑 mainlang은 미입력 시 기본값인 20, 파이썬으로 반환됨 
    print("이름 : {}, 나이 : {}, 메인 언어 : {}".format(name, age, mainlang))

profile("김밤송")


# 키워드값 이용해 함수 호출하기
def profile(name, age, mainlang) : 
    print(name, age, mainlang)

profile(mainlang="자바", age=20, name="김바미") #요렇게 값 전달할 때 순서 뒤죽박죽으로 해놔도 키워드 써두면 올바르게 출력됨


# 가변인자 (서로 다른 개수의 값 넣어도 그에 맞게 출력됨)
def profile(name, age, *language) :
    print("이름 : {}, 나이 : {}".format(name, age), end=" ") # end=" "는 print문마다의 줄넘김을 없애주고 쭉 이어서 출력되게 해줌
    for lang in language :
        print(lang, end=" ")
    print()

profile("밤송킴", 3, "파이썬", "자바스크립트", "자바")
profile("헤원킴", 23,"파이썬")        


# 지역변수(함수 내에서만, 즉 함수 호출될 때 생겼다가 함수 호출 끝나면 사라짐)와 전역변수(프로그램 내 모든 공간에서 사용 가능)
gun = 10 #전역변수 
def chkpoint(soldiers) :
    gun = 20 #이건 지역변수. 여기서 이거처럼 gun 초기화 안 해주면 냅다 이 함수 호출 시 오류 뜸
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))

print("전체 총 : {}".format(gun))
chkpoint(2)
print("남은 총 : {}".format(gun))


def chkpoint(soldiers) :
    global gun #이건 저 위의 전역변수 gun을 사용하겠다는 것.
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))

print("전체 총 : {}".format(gun))
chkpoint(2)
print("남은 총 : {}".format(gun)) 
# 그러나 전역변수를 많이 쓰면 코드 관리 어려워서 권장되진 않아. 그래서~ 밑을 보삼.


def chkpoint_ret(gun, soldiers) : #여기서의 gun도 지역변수긴 하지만? 일단 gun을 함수의 파라미터로 던져줌.
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))
    return gun #여기서 바뀌어진 gun의 값을 리턴시켜서 외부로 던질 수 있고!

print("전체 총 : {}".format(gun))
gun = chkpoint_ret(gun, 2) #요렇게 전역변수 gun을 chkpoint_ret함수에 전달해서 계산되고 반환된 값을 전역 gun에 다시 저장시킴!! 
print("남은 총 : {}".format(gun)) 



######퀴즈
def std_weight(height, gender) :
    if gender == "남자" :
        print("키 {} 남자의 표준 체중은 {}이다.".format(round(height*100), round(height*height*22, 2)))
    else :
        print("키 {} 여자의 표준 체중은 {}이다.".format(round(height*100), round(height*height*21, 2)))

std_weight(1.75, "남자")