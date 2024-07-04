# hello_world = "엄마가 말했다. '밥먹었니?'"
# print(hello_world)

# name = "홍길동"
# money = 100
# print("안녕하세요. ", name, "님 반갑습니다.")
# print("입력하신 금액은", money, "원 입니다.")

# 데이터 출력 시, % 기호 사용하는 방법
name = "임채원"
print("안녕하세요. 저의 이름은 %s입니다." %name )

money = 10000
print("입력하신 금액은 %d 원 입니다." %money)

a = 7
b = 3

result = a+b
print(result)

# 문자열 길이 구하기
hello_world = "엄마가 말했다. '밥먹었니?'"
print(len(hello_world))

# 문자열 슬라이싱
a = "Life is too short, You need Python"
print(a[7], a[-1])
print(len(a))
print(a[0:5])

# 문자열 치환
date = "2024.07.04"
print("바꾸기 전의 데이터 %s" %date)
date = date.replace(".","-")
print("바꾼 후의 데이터: ", date)

# 연습문제 6.
string = "abcd"
string = string.replace("a","A")
print(string)

# 연습문제 5.
a = "Python"
print(a[5]+a[4]+a[3]+a[2]+a[1]+a[0])

# 문자열 여러 줄 출력하기
자유로운_문자열 = "아무 문자열이나 한 번 입력해보세요.\n그런데 저는 문자열을 더 이상 입력하고 싶지 않고, 집에 가고 싶습니다."
print(자유로운_문자열)