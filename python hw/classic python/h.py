def get_range(a, pos):
    n = len(a)
    if pos >= n:
        return ((0, 0, 0), -1)

    if pos == n - 1:
        return ((a[pos], a[pos] + 1, 1), pos + 1)
    if a[pos] == a[pos + 1]:
        return ((a[pos], a[pos] + 1, 1), pos + 1)

    asc = True
    shift = 1
    step = a[pos + 1] - a[pos]
    start = a[pos]
    last = a[pos + 1]
    if a[pos] > a[pos + 1]:
        asc = False
        shift = -1

    pos += 2
    while pos < n:
        if asc:
            if a[pos] <= a[pos - 1]:
                break
        else:
            if a[pos] >= a[pos - 1]:
                break
        if last + step != a[pos]:
            break
        last = a[pos]
        pos += 1

    return ((start, last + shift, step), pos)


a = list(map(int, input().split()))

pos = 0
while True:
    ans, pos = get_range(a, pos)
    if pos == -1:
        break
    print(*ans)
