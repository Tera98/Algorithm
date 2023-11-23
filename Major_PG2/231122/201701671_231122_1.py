'''
11장 [상속과 다형성] 과제 1번 Template
'''


class Polynomial:
    def __init__(self, *args):  # *args : 여러개의 인자(arguments)를 받겠다는 의미
        self.coefficients = args
        self.max_order = len(args)

    def __repr__(self):
        if self.max_order == 1:
            return str(self.coefficients[-1])
        else:
            printer = ''
            for order, arg in zip(range(self.max_order - 1, 0, -1), self.coefficients):
                printer += f"{arg}x^{order} + "
            printer += f'{self.coefficients[-1]}'
            return printer


class DiffPoly(Polynomial):
    def differentiation(self, num):  # 미분 인자를 입력 받는다
        out, arg = 0, 0
        for i in range(self.max_order - 1, 0, -1):  # 고차항 부터 내려 오면서 연산 하도록 반복 구성
            out += self.coefficients[arg] * i * num ** (i - 1)  # 미분 연산
            arg += 1
        return out  # 계산값 반환


if __name__ == '__main__':
    poly = DiffPoly(4, 1, 2, 3)
    print(poly)
    print(poly.differentiation(2))
    print("-------------------\n학번 : 201701671\n이름 : 안원용")
