x, y, w, h = map(int, input().split())

if x > w:
    data1 = x - w
    data2 = w
    if y > h:
        data3 = y - h
        data4 = h
    else:
        data3 = h - y
        data4 = y
else:
    data1 = w - x
    data2 = x
    if y > h:
        data3 = y - h
        data4 = h
    else:
        data3 = h - y
        data4 = y

print(min(data1, data2, data3, data4))
