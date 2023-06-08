##### 퀴즈
class House :
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year) :
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self) :
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)
        # print("{} {} {} {} {}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year)) => 난 이렇게 했는데 위 코드가 훨 간결하네..

one = House("강남", "아파트", "매매", "10억", "2010년")
two = House("마포", "오피스텔", "전세", "5억", "2007년")
three = House("송파", "빌라", "월세", "500/50", "2000년")

one.show_detail()
two.show_detail()
three.show_detail()

# House.show_detail(one) => 이런 형식도 가능하네.




##### 예외 처리
try :
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자 : "))
    num2 = int(input("첫 번째 숫자 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError : 
    print("에러! 잘못된 값을 입력했습니다.")
except ZeroDivisionError as err :
    print(err) # ZeroDivisionError의 내용인 division by zero 출력됨.
except : # try문 실행 중에 위의 밸류에러, 제로디비전에러 이외의 모든 오류 발생 시 처리. 어떤 에런지 메시지 받고 싶으면
    # except Exceiption as err : print(err) 해주면 ㅇㅋ.
    print("알 수 없는 에러 발생!")


##### 오류 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("첫 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError # raise 통해 에러 만들고
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError: # 위에서 만든 밸류에러 발생 시 처리될 문장
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


##### 사용자 정의 예외 처리
class BigNumberError(Exception): # Exception 클래스 상속받는 BigNumberError 클래스 생성해주고~
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("첫 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # ("입력값 : {0}, {1}".format(num1, num2)) 이건 BigNumberError에서 print(err)하면 나오는 >> 에러 내용. <<
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)    



##### finally (예외 처리 구문에서 정상 수행되든 오류 뜨든 무조건 실행되는 문장)
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("첫 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError # raise함수 통해 에러 만들고
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError: # 위에서 만든 밸류에러 발생 시 처리될 문장
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
finally :
    print("계산기를 이용해 주셔서 감사합니다!")



##### 퀴즈
class SoldOutError(Exception) :
  pass # 이 안에서 딱히 처리할 건 없으니 pass로 걍 넘김.
        

try :
    chicken = 10
    waiting = 1
    while(True) :
        print("남은 치킨 : {}".format(chicken))
        order = int(input("치킨 몇 마리 주문하세요? : "))
        if order < 1 :
            raise ValueError
        elif order > chicken :
            print("주문량이 남은 치킨수보다 많아요.")
        else : 
            print("주문 완료되었습니다.")
            print("남은 치킨 : {}".format(chicken-order))
            chicken -= order

        if chicken <= 0 :
            raise SoldOutError("오늘 치킨 소진.")
        
except ValueError :
    print("잘못된 값을 입력하였습니다.")
except SoldOutError as errmsg:
    print(errmsg)
except :
    raise ValueError
