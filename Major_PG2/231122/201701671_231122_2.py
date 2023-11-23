'''
11장 [상속과 다형성] 과제 2번 Template
'''


class ReplaceInstance(list):
    def replace(self, target_data, new_data):
        for i in range(len(self)):  # 전 리스트 순회
            if self[i] == target_data:  # 리스트 중 타겟 데이터를 찾고
                self[i] = new_data  # 타겟을 원하는 값으로 대체


if __name__ == '__main__':
    x = ReplaceInstance([5, 10, 4, 5, 11, 40, 10, 4, 10])
    x.replace(10, 0)  # x.replace(바꾸려는 값, 바뀐 값)
    print(f'replaced_list : {x}')
    print("-------------------\n학번 : 201701671\n이름 : 안원용")
