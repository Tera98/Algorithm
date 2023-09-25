# 사용자 입력 부분
name = input("이름을 입력하세요: ")
height = int(input("키(cm)를 입력하세요: "))
weight = int(input("몸무게를 입력하세요:"))
BMI = weight / height / 100 / height / 100

# BMI 값에 따라 몸상태 출력
if BMI < 18.5:
    print(f"{name} 님의 BMI는 {BMI}이고 저체중에 속합니다.")
elif BMI <= 22.9:
    print(f"{name} 님의 BMI는 {BMI}이고 정상에 속합니다.")
elif BMI <= 24.9:
    print(f"{name} 님의 BMI는 {BMI}이고 과체중에 속합니다.")
elif BMI <= 29.9:
    print(f"{name} 님의 BMI는 {BMI}이고 비만에 속합니다.")
else:
    print(f"{name} 님의 BMI는 {BMI}이고 고도비만에 속합니다.")

print("학번 : 201701671\n이름 : 안원용")
