# 사용자 정보 입력 부분
univ = input("학교: ")
credit = int(input("수강 학점: "))
gpa = float(input("평점: "))
english = int(input("영어 성적: "))

# 다른 학교 필터링
if univ not in ('A', 'B', 'C'):
    print("잘못된 학교입니다.")
# A 학교 졸업 가능성 확인
elif univ == 'A':
    if credit >= 130 and gpa >= 2.5:
        print("졸업 가능합니다.")
    else:
        print("졸업 불가능합니다.")
# B 학교 졸업 가능성 확인
elif univ == 'B':
    if credit >= 140 and gpa >= 3.0 and english >= 750:
        print("졸업 가능합니다.")
    else:
        print("졸업 불가능합니다.")
# C 학교 졸업 가능성 확인
else:
    if credit >= 120 and gpa >= 2.3 and english > 600:
        print("졸업 가능합니다.")
    else:
        print("졸업 불가능합니다.")

print("학번 : 201701671\n이름 : 안원용")

