# 입력 부분
price = int(input("물건 값 입력 : "))
input_1000 = int(input("1000원 지폐 개수 : "))
input_500 = int(input("500원 동전 개수 : "))
input_100 = int(input("100원 동전 개수 : "))

# 거스름돈 계산 부분
exchange = input_1000 * 1000 + input_500 * 500 + input_100 * 100 - price

# 출력 계산 부분 "//"와 "%"를 사용하였다.
ex_500 = exchange // 500
ex_100 = exchange // 100 % 5
ex_10 = exchange // 10 % 10
ex_1 = exchange % 10

# 출력 부분
print(f"500원 = {ex_500} 100원 = {ex_100} 10원 = {ex_10} 1원 = {ex_1}")
print("학번 : 201701671\n이름 : 안원용")


