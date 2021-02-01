a = list(map(int, input().split()))
n = int(input())

sm = 0
i, j = 0, 0
bi, bj = 0, 0
best_dif = len(a) + 5

while True:
    if j == len(a):
        break
    while sm < n and j < len(a):
        sm += a[j]
        j += 1
    while sm >= n:
        sm -= a[i]
        i += 1

    if j - i < best_dif:
        best_dif = j - i
        bi = i
        bj = j

if sum(a) >= n:
    print(*a[bi - 1:bj])
