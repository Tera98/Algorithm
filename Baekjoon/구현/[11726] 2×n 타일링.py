n = int(input())

data = [1, 2]

for i in range(n - 2):
    data.append(data[i] + data[i + 1])

print(data[n - 1] % 10007)
