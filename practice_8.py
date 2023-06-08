#####표준 입출력
print("Python", "Java", sep=" vs ", end="?")
#위에서 sep=" vs " 없었다면 걍 평소대로 Python Java 이렇게 출력되었을 것임. end="?"가 있어서 줄 안 넘어가고 ?로 문장 마무리됨.
print("뭐가 더 재밌을까?")

import sys
print("김밤송", "예뻐", file=sys.stdout) #표준출력
print("김밤송", "예뻐", file=sys.stderr) #표준에러


#정렬
scores = {"수학" : 90, "코딩" : 100, "불어" : 0}
for subject, score in scores.items() :
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust(숫자)는 총 숫자만큼의 공간을 확보하고 왼쪽으로 정렬하라는 것. 정렬은 문자형에만 되는 듯? rjust(숫자)도 똑같은데 오른쪽 정렬.


# 은행 대기번호처럼 0 채우기 (001, 002처럼)
for num in range(1,21) :
    print("대기번호 : " + str(num).zfill(3)) # 세 자리로 0채우겠다


# 표준 입력인 input()으로 입력받으면 문자열로 저장됨. 그래서 예를 들어 10 입력 후 숫자로 쓰려면 int()로 감싸줘야.



########다양한 출력 포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시 => + 넣어주면 됨
print("{0: >+10}".format(+500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))
# 3자리마다 콤마를 찍어주기
print("{0:,}".format(1000000000000))
# 3자리마다 콤마 찍고 +- 부호도 붙이기
print("{0:+,}".format(+1000000000000))
print("{0:+,}".format(-1000000000000))
# 3자리 마다 콤마를 찍어주고, 부호도 붙이고, 자릿수 확보하기, 빈 자리는 ^로 채우기
print("{0:^<30,}".format(1000000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시 (소수점 셋째 자리에서 반올림. 즉 소수점 둘째자리까지만 표현)
print("{0:.2f}".format(5/3))


# 파일 입출력
score_file = open("score.txt", "w", encoding="utf-8") # score.txt파일을 w(쓰기 목적)으로 열겠다.(score.txt 파일 생성됨) utf-8 안 써주면 한글파일 깨질 수도. 
print("수학 : 90", file=score_file)
print("영어 : 100", file=score_file)
score_file.close() # 파일 열었을 땐 닫아주는 것까지 해줘야 됨

score_file = open("score.txt", "a", encoding="utf-8") # 또 w로 해주면 덮어쓰기 되는데 이미 존재하는 파일에 이어쓰고 싶으면 append의 약자인 "a"로 정의해줌.
score_file.write("코딩 : 100")
score_file.write("\n과학 : 95") # .write로 해주면 줄바꿈 기능 안 돼서 \n 넣어준것
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.read()) # read함수 호출해주면 파일의 모든 내용 한 번에 읽어와서 출력해줌
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline()) # readline함수는  한 줄 읽고 커서를 다음 줄로 이동. 줄바꿈 안 하고 싶으면 .readline(), end="" 해주면 됨
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

# 만약 readline()으로 한 줄씩 읽을 때 총 몇 줄인지 모를 때 
score_file = open("score.txt", "r", encoding="utf8")
while True :
    line = score_file.readline()
    if not line : # line이 없다면, 즉 읽어온 내용이 없을 때
        break
    print(line) # 라인에 내용이 있다면 걍 출력
score_file.close()  


# 리스트에 값 넣어 처리
core_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 줄을 line란 이름의 list형태로 저장
for line in lines: # line이란 변수 만들고 lines란 리스트에서 하나씩 불러와서 출력
    print(line, end="")

score_file.close()

