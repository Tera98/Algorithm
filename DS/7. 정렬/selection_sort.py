def selection_sort(a):
    cnt_com, cnt_swap = 0, 0
    for i in range(0, len(a) - 1):
        minimum = i
        for j in range(i, len(a)):
            if a[minimum] > a[j]:
                minimum = j
                cnt_com += 1
        a[i], a[minimum] = a[minimum], a[i]
        cnt_swap += 1
    return cnt_com, cnt_swap


# a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
# print('정렬 전\t', end='')
# print(a)
# selection_sort(a)
# print('정렬 후\t', end='')
# print(a)
