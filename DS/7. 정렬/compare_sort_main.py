from insertion_sort import insertion_sort
from selection_sort import selection_sort

b = [10, 11, 17, 17, 17, 20, 22, 26, 31, 44, 49, 54, 77, 77, 88, 93]
print('정렬 전:\t', end='')
print(b)
[cnt_com, cnt_swap] = insertion_sort(b)
print('정렬 후:\t', end='')
print(b)
print('Comparisons:\t %d\n' % cnt_com, end='')
print('Swaps:\t %d\n' % cnt_swap, end='')

c = [93, 88, 77, 77, 54, 49, 44, 31, 26, 22, 20, 17, 17, 17, 11, 10]
print('정렬 전:\t', end='')
print(c)
[cnt_com, cnt_swap] = insertion_sort(c)
print('정렬 후:\t', end='')
print(c)
print('Comparisons:\t %d\n' % cnt_com, end='')
print('Swaps:\t %d\n' % cnt_swap, end='')

d = [10, 11, 17, 17, 17, 20, 22, 26, 31, 44, 49, 54, 77, 77, 88, 93]
print('정렬 전:\t', end='')
print(d)
[cnt_com, cnt_swap] = selection_sort(d)
print('정렬 후:\t', end='')
print(d)
print('Comparisons:\t %d\n' % cnt_com, end='')
print('Swaps:\t %d\n' % cnt_swap, end='')

e = [93, 88, 77, 77, 54, 49, 44, 31, 26, 22, 20, 17, 17, 17, 11, 10]
print('정렬 전:\t', end='')
print(e)
[cnt_com, cnt_swap] = selection_sort(e)
print('정렬 후:\t', end='')
print(e)
print('Comparisons:\t %d\n' % cnt_com, end='')
print('Swaps:\t %d\n' % cnt_swap, end='')