import random

# 공백 기준 리스트 입력
my_num = list(map(int, input("당신의 번호를 입력하세요 : ").split()))

# 당첨 번호 및 보너스 번호 추출
numbers = []
while len(numbers) <= 6:  # 총 45개의 번호 중 7개 랜덤 추출
    tmp = random.randint(1, 45)
    if tmp not in numbers:  # 리스트에 존재하지 않는 번호만 추가
        numbers.append(tmp)

win_numbers = numbers[0:6]  # 당첨 번호는 앞 6개
bonus_number = numbers[6]  # 보너스 번호는 마지막 1개


def lotto(my_num, win_numbers, bonus_number):  # 일치하는 번호 찾기
    same_cnt = 0
    for num in win_numbers:  # 당첨 번호 포함 여부
        if num in my_num:
            same_cnt += 1
    if same_cnt == 6:
        return 1
    elif same_cnt == 5:
        if bonus_number in my_num:
            return 2
        else:
            return 3
    elif same_cnt == 4:
        return 4
    elif same_cnt == 3:
        return 5
    else:
        return 6


result = lotto(my_num, win_numbers, bonus_number)

# 결과 확인
print(f"당첨 번호: {win_numbers}, 보너스: {bonus_number}")
print(f"나의 번호 : {my_num}")
if result == 1:
    print("축하합니다! 1등입니다.")  # 6개 당첨
elif result == 2:
    print("축하합니다! 2등입니다.")  # 5개+보너스 당첨
elif result == 3:
    print("축하합니다! 3등입니다.")  # 5개 당첨
elif result == 4:
    print("축하합니다! 4등입니다.")  # 4개 당첨
elif result == 5:
    print("축하합니다! 5등입니다.")  # # 3개 당첨
else:
    print("아쉽게도 당첨되지 않았습니다.")  # 2개 이하

print("-------------------\n학번 : 201701671\n이름 : 안원용")
