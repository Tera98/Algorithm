def remove_duplicates(lst):
    # 중복 제거 코드
    tmp = set(lst)  # 리스트 자료구조를 set 자료구조로 바꾸면 중복 제거와 오름차순 정렬이 진행된다.
    lst = list(tmp)  # 다시 리스트로 변환후 반환한다.
    return lst


def second_largest(lst):
    # 두 번째로 큰 값 검출
    num = lst[-2]  # 오름차순
    return num


lst = [5, 9, 1, 2, 4, 1, 0, 9, 7]
lst = remove_duplicates(lst)
print(second_largest(lst))  # Expected output: 7

print("-------------------\n학번 : 201701671\n이름 : 안원용")
