##### 모듈

import theater_module
theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이서 조조 할인 영호 보러 갔을 때
theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

import theater_module as mv # 위에서 theater_module. 이걸 계속 썼는디 이게 모듈명이 너무 기니까 theater_module의 별명으로 as 붙여줌. 이렇게 쓰면 theater_module을 mv로만 호출 가능
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

# 위와는 또 다른 방법으로 from ~ import 구문이 있음!
# 이걸론 앞에 theater_module 붙일 필요 X. import *로 이 모듈의 모든 걸 사용하겠다고 해뒀으니 바로 price(3) 이런 식으로 쓰면 됨. 
from theater_module import * # * 이걸로 전체 기능 불러옴
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning # 모듈 부르고 군인가격은 필요 없어서 price, price_morning만 꺼냄
price(5)
price_morning(6)
price_soldier(7) # 여기선 오류남

from theater_module import price_soldier as price # 군인가격만 알고 싶은데 price_soldier도 길어서 별명 붙여주기.
price(5)




##### 패키지 (모듈 모아놓은 것. 하나의 디렉토리에 여러 모듈 파일들 갖다둔 게 패키지라 생각하면 됨)
import travel.thailand # import 쓸 때 주의점 : import 웅앵 할 때 웅앵 오른쪽 끝엔 패키지나 모듈만 올 수 있음. 클래스나 함수는 import 불가. 그러나 from ~ import 구문에선 사용 가능. 아래처럼!
trip_to = travel.thailand.ThailandPackage() # travel 패키지 속 thailand 모듈 속의 ThailandPackage() 클래스로 trip_to라는 객체 생성
trip_to.detail()

from travel.thailand import ThailandPackage # from ~ import 구문에선 패키지, 모듈, 함수, 클래스 다 import 가능. 여기선 클래스 import했음.
trip_to = ThailandPackage() # 이땐 클래스로 바로 객체 생성 가능.
trip_to.detail()

from travel import vietnam # 모듈 import 했음.
trip_to = vietnam.VietnamPackage()
trip_to.detail()



##### __all__
from travel import *
trip_to = vietnam.VietnamPackage() # => __init__.py에서 암것도 안 써준 상태에서는 이렇게 travel에서 모든 걸 갖고 오겠다고 위에서 써줬는데도 여기서 오류나는데, 왜냐면 개발자가 이 문법상에서 공개범위 설정 안 해줘서임. 패키지 안에 포함된 것들 중에서 import되길 원하는 것들만 공개를 하고 원하지 않는 건 비공개로 할 수 있음.
# __init__.py 가서 __all__ = ["vietnam", "thailand"] 이렇게 두 모듈 쓸 수 있게 해줘야 오류 안 남.
trip_to.detail()
trip_to = thailand.ThailandPackage() # __init__.py에  __all__ = ["vietnam", "thailand"] 이 속에 타일랜드 모듈도 쓰게 해놔서 오류 안 나는 거.
trip_to.detail()



##### 모듈 직접 실행
# thailand.py 가서 확인!


##### 패키지, 모듈 위치
import inspect
import random
print(inspect.getfile(random)) # random이란 모듈이 어느 위치에 있나 파일 정보 알려줌
print(inspect.getfile(thailand))



##### pip install (패키지 설치)
# pypi란 사이트가 있음! 거기서 복사하고 터미널에 붙여넣기 하면 다운받아짐. 그리고 터미널에 pip list 입력하면 현재 설치되어 있는 패키지 확인 가능. 그리고 pip show 패키지이름 입력하면 해당 패키지 정보 알려줌. 또 pip install --upgrade 패키지이름 입력하면 해당 패키지 업그레이드 가능. 그리고 패키지 삭제하려면 pip uninstall 패키지이름 입력하면 y/n? 뜨고 y 입력하면 삭제됨.



##### 내장함수 (따로 import할 필요 없이 내장돼 있으니 바로 사용 가능)
# 예시들
# input() : 입력받고 문자열로 저장
# dir() : 어떤 객체 넘겨줬을 때 그 객체가 어떤 변수와 함수 가지고 있는지 표시

print(dir())
import random # 외장 함수
print(dir()) # 위의 print(dir())와 비교하면 random도 추가돼서 출력됨. 사용할 수 있는 것에 추가된 거지. 
import pickle
print(dir()) # 사용할 수 있는 목록에 pickle 추가됨

print(dir(random))
# random. 했을 때 사용할 수 있는 것들 리스트가 나옴

lst = [1, 2, 3]
print(dir(lst)) # lst가 쓸 수 있는 것들 목록 나옴 append 등...

name = "BAMSONG"
print(dir(name)) # name이 쓸 수 있는 것들 목록 나옴 split 등...
# 구글에 list of python builtins 검색하면 내장함수들 리스트 쫙 나옴



##### 외장함수 (직접 import해서 사용해야 함)
# 구글에 list of python modules 검색하면 외장함수 목록 나옴.
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py")) # 여기 python workspace 내 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리 위치

folder = "sample_dir" # folder변수 생성

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder) # sample_dir 폴더 삭제
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) # sample_dir 폴더 생성
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir()) # glob과 비슷한 기능, 디렉토리 파일, 폴더 존재하는 내용 표시

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후



##### 퀴즈
from mymodule import byme
mysign = byme.Otsukaresama()
mysign.sign()