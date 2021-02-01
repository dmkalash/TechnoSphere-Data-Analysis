n, k = map(int, input().split())

sm = 0
for i in range(1, k + 1):
    sm += int(str(n) * i)

print(sm)
