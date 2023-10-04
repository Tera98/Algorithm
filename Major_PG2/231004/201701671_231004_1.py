# 주어진 행렬 입력
mat = [[1019, 223, 315, 421], [503, 621, 711, 805], [900, 1000, 112, 128], [137, 753, 555, 426]]


# 정규화 함수
def normalize_4x4_matrix(mat):
    min_value = min(map(min, mat))  # map 함수로 각 리스트 원소의 최솟값을 반환하고, 그 반환값 중의 최솟값을 구한다.
    max_value = max(map(max, mat))  # 위와 같은 방식으로 최댓값을 정한다.
    for i in range(4):  # 최솟값을 빼고 정해진 값으로 나누는 정규화 과정을 실시한다.
        for j in range(4):
            mat[i][j] -= min_value
            mat[i][j] = round(mat[i][j] / (max_value - min_value), 8)
    return mat


result_mat = normalize_4x4_matrix(mat)
print(*result_mat, sep="\n")  # 보기 쉽게 \n을 추가하였다
print("-------------------\n학번 : 201701671\n이름 : 안원용")
