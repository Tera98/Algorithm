# 사용자 입력 부분
price = int(input("물건의 가격: "))
coupon = input("쿠폰 번호: ")
output = price

# 쿠폰 번호에 따라 할인 가격 결정
if coupon == "ABCD":
    if price >= 5000:
        output *= 0.9
elif coupon == "EFGH":
    if price >= 7000:
        output *= 0.75
    elif price >= 5000:
        output -= 1000
elif coupon == "ZXCV":
    output *= 0.5

# 결과 출력
print(f"할인된 가격은 {int(output)}원 입니다.\n학번 : 201701671\n이름 : 안원용")
