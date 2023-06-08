#리스트[] (순서를 가지는 객체의 집합)
#지하철 칸별로 10,20,30명

subway1 = 10
subway2 = 20
subway3 = 30

#이거를

subway = [10, 20, 30] # subway라는 리스트 생성
print(subway)

subway = ["헤원", "밤송", "송밤"]
print(subway.index("밤송")) #밤송은 몇 번째 칸에 타고 있는가?
subway.append("인자") #엄마도 탑승
print(subway)
subway.insert(1, "카티") #카티를 헤원/밤송 사이에 태움
print(subway)
print(subway.pop()) #한 명씩 뒤에서 꺼냄 (출력하고 빠짐)
print(subway)
print(subway.pop())
print(subway)
subway.append("헤원")
print(subway.count("헤원")) #"헤원"이 몇 개인가?


numlist = [4,5,2,1,3]
numlist.sort() # 오름차순 정렬 .sort()
print(numlist)
numlist.reverse() # 뒤집기 .reverse()
print(numlist)
numlist.clear() # 리스트 모든 내용 비우기 ( []만 남음 )
print(numlist)

#리스트는 여러 자료형 공존 가능
mixlist = ["밤송", 2, True]
print(mixlist)
haha = [2,3,4]
mixlist.extend(haha) #리스트 확장
print(mixlist)
# print(mixlist + haha) => 요렇게 리스트끼리 합치기도 가능




###########
#딕셔너리 {}
cabinet = {3 : "히데", 5 : "혜원"} # 3,5가 key, 히데,혜원이 value
print(cabinet[3]) # 히데 출력
print(cabinet.get(3)) # 위와 똑같이 히데 출력
# print(cabinet[100]) => 없는 키 입력시 오류나고 프로그램 종료됨
# print(cabinet.get(100)) => 오류 대신 None 뜨고 프로그램 종료 안 되고 계속 이어나갈 수 ㅇㅇ.
# print(cabinet.get(100, "hihi")) => None 대신 hihi뜸
print(3 in cabinet) # cabinet에 3키 있느냐 : True
print(30 in cabinet) # 30번키 없으니 False
# 딕셔너리 키는 정수 말고도 "A-3" 이런 문자열형식도 가능.

#딕셔너리 추가
cabinet["C-7"] = "공주밤송" # 똑같은 형식으로 cabinet[3] = "카티" 이렇게 값 업데이트도 가능.
print(cabinet)

#딕셔너리 삭제
del cabinet[3]
print(cabinet)

print(cabinet.keys()) #딕셔너리 key들만 출력
print(cabinet.values()) #딕셔너리 value들만 출력
print(cabinet.items()) #딕셔너리 key,value 쌍으로 출력
cabinet.clear() # 딕셔너리 비워서 {}만 남음
print(cabinet)




##########
#튜플 (튜플은 내용 변경,추가 안 됨. but 속도는 리스트보다 빠름)

menu = ("수플레", "푸딩") #이걸로 값 고정됨
print(menu[0])
print(menu[1])
# menu.add("케이크") => 이런 거 추가 안 됨
(name, age, hobby) = ("김밤송", 3, "먹기")
print(name, age, hobby)



#######
# 집합(세트) {} => 중복X, 순서X
myset = {1,2,3,3,3}
java = {"이상혼", "김밤송", "밤공주"}
python = set(["김혜원", "송이왕자", "김밤송"]) #요렇게 리스트에 쓰고 set()로 감싸도 집합 정의됨

#교집합
print(java&python) # {'김밤송'} 출력
print(java.intersection(python))

#합집합
print(java|python)
print(java.union(python))

#차집합
print(java-python)
print(java.difference(python))

#집합에 항목추가
python.add("헤지")
print(python)

#집합 항목 지우기
python.remove("헤지")
print(python)



#######
# 자료구조의 변경
menu = {"수플레", "푸딩", "주스"}
print(menu, type(menu)) # type()은 자료 형태 알려줌

menu = list(menu) # 집합에서 리스트로 바뀜. tuple()로 감싸면 튜플 되고.
print(menu, type(menu))

menu = set(menu)