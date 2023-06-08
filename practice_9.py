######## pickle (프로그램상에서 우리가 사용하고 있는 데이터를 파일형태로 저장해주는 것)
import pickle
profile_file = open("profile.pickle", "wb")
# profile.picle 파일 생김
# b : pickle에서는 binary 타입 정의 반드시 해야함, 인코딩 설정 안해도 됨
profile = {"이름" : "박명수", "나이" : 30, "취미" :["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile,profile_file) # 피클을 이용해 데이터를 파일에 써줌. dump(파일에 저장할 데이터 내용, 저장되는 그 파일) 
profile_file.close()

profile_file = open("profile.pickle", "rb") # 쓰기 아닌 읽기로 profile.pickle파일 가져옴
profile = pickle.load(profile_file) # 파일 내용 그대로 가져와서 데이터 형태로 불러와줌 (load를 통해 file에 있는 정보를 profile에 불러옴)
print(profile)
profile_file.close()



####### with (파일 쓰고 읽는 것도 각 두 줄씩이라 짧고 간결, 매번 close해줄 필요도 X. 수월히 파일 처리)
import pickle # with문은 마지막에 파일을 자동으로 close 해준다.
with open("profile.pickle", "rb") as profile_file: #파일 열고 이 파일 정보를 profile_file이란 변수에 저장
    print(pickle.load(profile_file)) # load를 통해 profile_file를 불러와 출력

# 피클 안 쓰고 일반적인 파일 쓰고 읽을 때 with 써보기
with open("study.txt", "w", encoding="utf8") as study_file: # 파일 정보 study_file에 저장 (study.txt 생성됨!)
    study_file.write("파이썬을 열심히 공부하고 있어요") 

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read()) # study_file에 있는 내용을 read함수 통해 읽어와 출력



#########퀴즈
# for i in range(1, 51) :
#     with open("{}주차.txt".format(i), "w", encoding="utf8") as bogo_file : # 파일 정보 bogo_file에 저장 ({}주차.txt 생성됨!)
#         bogo_file.write("- {}주차 주간 보고 -\n부서 : \n이름 : \n업무 요약 : ".format(i)) # 아니면 bogo_file.write(\n 포함해서)를 4줄 써줘도 ㅇㅋ.

# 여기서 파일들 한꺼번에 지우려면 1주차.txt 누르고 쉬프트 누른 상태에서 50주차.txt 누르면 한꺼번에 선택됨!