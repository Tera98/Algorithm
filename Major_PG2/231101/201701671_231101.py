class Calculator:

    # problem 1
    def __init__(self):  # 계산 값과 초기 기록 초기화
        self.val = 0
        self.his = []

    def add(self, num):  # add
        self.val += num
        return self.val

    def subtract(self, num):  # subtract
        self.val -= num
        return self.val

    def multiply(self, num):  # multiply
        self.val *= num
        return self.val

    def divide(self, num):  # divide, 0으로 나눌 수 없는 부분 추가
        if num == 0:
            print("Error: Division by zero")
        else:
            self.val /= num
            return self.val

    def clear(self):  # 값 초기화
        self.val = 0

    # problem 2
    def add_history(self, operation):  # 기록 add, 문자열 그대로 리스트에 저장
        self.his.append(operation)

    def clear_history(self):  # 기록 초기화
        self.his = []

    def print_history(self):  # 기록 출력
        if len(self.his) != 0:
            for i, j in enumerate(self.his):  # enum 활용해 인덱스와 같이 출력하게 함
                print(str(i + 1) + ": " + j)
        else:
            print("No operation history")  # 기록 없는 경우

    # probelm 3
    def solve_quadratic(self, a, b, c):
        pass
        # return


def main():  # 1, 2번 풀이
    problems = list(input('어떤 문제를 풀건가요? : (예시 1,2,3)'))

    problem_2 = '2' in problems  # 문제 2번 선택
    problem_3 = '3' in problems  # 문제 3번 선택

    # instance
    calc = Calculator()
    active = True if '1' in problems else False

    information = "\nOptions: 'add', 'subtract', 'multiply', 'divide', 'clear', 'quit'"
    if problem_2:
        information += ", 'history'"
    if problem_3:
        information += ", 'quadratic'"

    # 계산기 출력!
    while active:
        print(information)
        command = input("Enter the command: ").upper()

        # Problem 1
        if command in ['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE']:
            num = float(input("Enter the number: "))
            if command == 'ADD':
                res = calc.add(num)
                print("Result:", res)
            elif command == 'SUBTRACT':
                res = calc.subtract(num)
                print("Result:", res)
            elif command == 'MULTIPLY':
                res = calc.multiply(num)
                print("Result:", res)
            elif command == 'DIVIDE':
                res = calc.divide(num)
                if res is not None:  # 0으로 나누기를 방지
                    print("Result:", res)

            # Problem 2, history 기록
            if res is not None and problem_2:
                calc.add_history(f"{command:8s} {num} : Result {res}")

        # Problem 2, history 출력
        elif command == 'HISTORY' and problem_2:
            print("\nOperation History:")
            calc.print_history()

        # Problem 1, 계산기 초기화
        elif command == 'CLEAR':
            calc.clear()
            if problem_2:
                calc.clear_history()

        # 계산기 종료
        elif command == 'QUIT':
            active = False
            print("-------------------\n학번 : 201701671\n이름 : 안원용")

        # Problem 3
        elif command == 'QUADRATIC' and problem_3:
            print("Enter the coefficients of the equation ax^2 + bx + c = 0")
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))

            if a == 0:  # 계수 a가 0이면, 예외처리.
                print("This is not a quadratic equation. 'a' should not be zero.")
            else:
                root1, root2 = calc.solve_quadratic(a, b, c)
                print(f"The solutions are {root1} and {root2}")
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
