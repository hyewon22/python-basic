########클래스

# # 마린 : 공격 유닛, 군인, 총 쏨
# name = "마린" #유닛 이름
# hp = 40 #체력
# damage = 5 #공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name ="탱크"
# tank2_hp = "150"
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format( \
#         name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)



#일반 유닛
class Unit : # Unit이란 클래스 정의
    def __init__(self, name, hp, damage) : # self는 자기 자신을 의미. 메소드 앞에는 항상 이렇게 써줘야 됨. >> self. << 을 통해서 자기 자신의 변수에 접근 가능.
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        # __init__함수로 (객체 정의에) 필요한 값들 정의해줌

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
#요렇게 하나의 같은 클래스로 서로 다른 마린,탱크를  만들어냄.


##### __init__ 함수 (파이썬에서 생성자. 마린,탱크 같은 >>객체 만들어질 때 자동으로 호출<<됨) +객체란? 마린,탱크처럼 클래스로부터 만들어진 애들. 이때 마린,탱크는 Unit클래스의 인스턴스라고 함. 객체가 생성될 땐 그 인자값의 수가 기본적으로 함수에 정의된 파라미터개수와 동일해야 객체 만들 수 있음. (self는 제외하고)
# 즉 여기선 marine3 = Unit("마린") 이렇게만 할 수 없고 40, 5도 넣어줘야 한다는 거임.


##### 멤버 변수
# self.name, self.hp, self.damage 여기서 name, hp, damage 얘네가 멤버변수임. 멤버변수란? self.와 함께 사용할 수 있음. 어떤 클래스 내에서 정의된 변수. 그 변수를 가지고 우리가 실제로 초기화할 수 있고 사용도 할 수 있는.

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 클래스 외부에서도 멤버변수 사용 가능! 외부에선 요렇게 >> 객체명. << 을 통해 멤버변수에 접근 가능.

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 위 실제 Unit클래스엔 clocking변수 없었는데 우리가 외부에서 wraith2에 clocking이란 변수를 추가로 할당해서, True값 넣은 거임. 이렇게 파이썬에선 어떤 객체에 추가로 변수를 외부에서 만들어 쓸 수 있음. wraith2에 만든 거지, wraith1에는 안 된 것임! 기존의 다른 객체엔 적용 안 됨~

if wraith2.clocking == True:
    print("{} 는 현재 클로킹 상태입니다.".format(wraith2.name))




##### 메소드, 상속
#메딕 유닛 (상속부분에서 쓸 건데 걍 내가 만듦)
class MedicUnit :
    def __init__(self, name, hp) :
        self.name = name
        self.hp = hp

#공격 유닛
class AttackUnit(MedicUnit) : # AttackUnit은 MedicUnit로부터 상속받은 자식 클래스.
    def __init__(self, name, hp, damage) :
        # self.name = name
        # self.hp = hp 얘네는 MedicUnit의 __init__과 같은 거니 부모 걸로 쓰면 됨. 즉,
        MedicUnit.__init__(self, name, hp) # 이렇게 해주면 MedicUnit의 __init__을 그대로 사용.
        self.damage = damage
        # __init__함수는 결국 이 클래스에서 객체 생성할 때 담겨야 하는 값들을 정의하는 것 같군.
    
    def attack(self, location) :
         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage)) # self.name, self.damage는 클래스에 있는 변수의 값을 출력하는 것임. location은 전달받은 값 그대로 쓰는 거고.

    def damaged(self, damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
            if self.hp <=0:
                print("{0} : 파괴되었습니다.".format(self.name))         

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16) # AttackUnit클래스를 통해 firebat1 객체 생성.
firebat1.attack("5시") 

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)



##### 다중 상속 (부모클래스 2개 이상)
# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격은 X

# 날 수 있는 기능을 가진 클래스
class Flyable :
    def __init__(self, flying_speed) :
          self.flying_speed = flying_speed

    def fly(self, name, location):
            print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
                .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 이 두 클래스에서 제공하는 모든 것들 사용 가능
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
           
# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시") # name은 Flyable클래스에 멤버변수로 없어서 valkyrie.name이라고 별도로 추가해준 거고, self.로 있는 멤버변수는 이렇게 안 써줘도 됨
valkyrie = AttackUnit("발키리", 200, 6)
valkyrie.attack("5시")           
            




##### 메소드 오버라이딩 (부모클래스에서 정의한 메소드 아닌 자식클래스에서 정의한 메소드 사용하고 싶을 때. 자식클래스에서 메소드 재정의)

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # 상속 받음
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격은 X
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0 (지상 speed 없으니까 걍 0으로 넣어줌)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location) # fly 함수가 있는 flyable클래스를 상속받고 있으니 걍 self.fly 해주면 알아서 flyable클래스 참조됨.

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")        



##### pass (패스)
# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 아무것도 하지 않고 일단 걍 넘어가겠다

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") # 실행하면 아무것도 안 일어나고 걍 프로그램 끝남.

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()




##### super

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0) => 건물은 speed 없으니 0으로. 근데 이렇게도 쓸 수 있지만 super로 써보자면~
        super().__init__(name, hp, 0) # super는 super() 요렇게 괄호 붙이고, self 안 씀!
        self.location = location


# super를 연습해보자~!
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() -> 요렇게 super 쓰면 상속받는 클래스 중 맨 처음인 "Unit 생성자"만 출력됨. 즉 class FlyableUnit(Unit, Flyable) 여기서 Unit이 맨 앞에 있어서. Flyable이 맨 앞이면 그 반대고. 이런 문제 때문에 다중상속 받을 때, 그리고 모든 부모클래스에 대해 초기화 할 땐 따로 아래줄처럼 할 것.
        Unit.__init__(self)
        Flyable.__init__(self)       