def award_counter(awards):
    counter = {}  # 빈 딕셔너리 선언
    for set_line in awards:
        for person in set_line:
            if person in counter.keys():
                counter[person] += 1  # 키가 있는 경우
            else:
                counter[person] = 1  # 키가 없는 경우

    count = 0
    for i in counter.values():
        if count < i:
            count = i               # 최다 수상 개수 저장

    for k, v in counter.items():
        if v == count:
            print(f'최다 수상자는 {k}로, 총 {v}개 수상하였습니다!') # 최다 수상자 출력


award1 = {'A', 'B', 'C'}
award2 = {'B', 'C', 'D'}
award3 = {'F', 'E', 'B'}
award4 = {'A', 'B', 'D', 'G'}
award5 = {'D', 'G'}
award6 = {'A', 'C', 'D'}
award_counter([award1, award2, award3, award4, award5, award6])

print("-------------------\n학번 : 201701671\n이름 : 안원용")
