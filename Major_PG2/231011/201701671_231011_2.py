INF = 10e11


def min_sublist_sum(lst):
    min_value = INF
    min_add = 0, 0
    # 코드 작성
    for j in range(1, len(lst)):
        sum_lst = [INF] * len(lst)
        sum_lst[j - 1] = lst[j - 1]
        for i in range(j, len(lst)):
            sum_lst[i] = sum_lst[i - 1] + lst[i]
            if min_value > min(sum_lst):
                min_value = min(sum_lst)
                min_add = j, sum_lst.index(min(sum_lst))

    return min_value, lst[min_add[0] - 1:min_add[1] + 1]


print(min_sublist_sum([4, 1, -3, 1, -2, -3, 1, -2, 4]))
print(min_sublist_sum([1, 2, 3, 4]))
print("-------------------\n학번 : 201701671\n이름 : 안원용")
