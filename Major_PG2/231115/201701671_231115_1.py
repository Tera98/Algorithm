n = int(input())
data = []
for _ in range(n):
    data.append(list(input().split()))      # 공백 기준 split 해서 list로 추가

data = sorted(data, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))        # lambda 사용 정렬

for i in data:
    print(i[0])

print("-------------------\n학번 : 201701671\n이름 : 안원용")
