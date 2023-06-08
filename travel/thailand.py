class ThailandPackage :
    def detail(self) :
         print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__" :
     print("이 문장은 thailand 모듈을 직접 실행할 시에만 출력돼요") # thailand.py에서 코드 수정하고 직접 실행할 때만 이 구문 나옴
     trip_to = ThailandPackage()
     trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출") # thailand.py에서 ThailandPackage 클래스 갖다 쓸 땐 "Thailand 외부에서 모듈 호출" 출력되고, thailand.py에서 직접 코드 수정하고 직접 실행할 땐 "이 문장은 thailand 모듈을 직접 실행할 시에만 출력돼요" 출력됨.