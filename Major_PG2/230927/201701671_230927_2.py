# 기존 matrix 설정

matrix_A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix_B = [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
matrix_3D = [matrix_A, matrix_B]

# 삼중 for문을 구현 하여 10의 위치를 확인 하는 코드
for i in range(2):  # Z
    for j in range(4):  # Y
        for k in range(4):  # X
            if matrix_3D[i][j][k] == 10:
                print(f"찾은 원소 10은 X={k}, Y={j}, Z={i}에 존재합니다.")

print("학번 : 201701671\n이름 : 안원용")
