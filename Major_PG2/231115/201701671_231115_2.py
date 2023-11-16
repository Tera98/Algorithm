import random
import time

cnt, cnt_time = 0, 0
for i in range(5):
    a = random.randint(1, 100)        # 랜덤 정수값 생성
    b = random.randint(1, 100)
    cal = random.randint(1, 4)          # 연산 선택
    start_time = time.time()              # 시작 시각 측정
    tmp = False         # 정답 판별 변수
    if cal == 1:        # 덧셈
        output = int(input(f"{a} + {b} \n = "))
        if output == a + b:
            tmp = True
        else:
            out = eval("a+b")  # 오답 시  출력
    elif cal == 2:      # 뺄셈
        output = int(input(f"{a} - {b} \n = "))
        if output == a - b:
            tmp = True
        else:
            out = eval("a-b")
    elif cal == 3:      # 곱셈
        output = int(input(f"{a} * {b} \n = "))
        if output == a * b:
            tmp = True
        else:
            out = eval("a*b")
    else:       # 나눗셈
        output = float(input(f"{a} / {b} \n = "))
        if output == a / b:
            tmp = True
        else:
            out = eval("round(a/b,2)")
    runtime = round(time.time() - start_time, 2)  # 실행 시간
    print(f"문제 {i + 1} 번을 푸는데 걸린 시간 : {runtime} 초")
    if tmp:
        print("정답!")
        cnt += 1        # 정답 개수 측정
    else:
        print(f"오답!\n{out}")
    cnt_time += runtime         # 총 시간 측정

print(f"모든 문제를 푸는데 걸린 시간 : {round(cnt_time, 2)} 초\n정답 : {cnt} 오답 : {5 - cnt}")
print("-------------------\n학번 : 201701671\n이름 : 안원용")
