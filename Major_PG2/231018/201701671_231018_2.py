def first_non_repeated(s):
    counter = {}
    for i in s:
        if i in counter.keys():
            counter[i] += 1  # 키가 있는 경우
        else:
            counter[i] = 1  # 키가 없는 경우

    for k, v in counter.items():  # 한번 입력된 첫 문자를 반환하는 부분
        if v == 1:
            return k

    return 'None'  # 모두 반복되는 부분일 경우 None 반환


print(first_non_repeated("swiss"))
# Expected output: “w”
print(first_non_repeated("noon"))
# Expected output: None
print("-------------------\n학번 : 201701671\n이름 : 안원용")
