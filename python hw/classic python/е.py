def get_string(lst):
    res = ''
    for c in lst:
        res += c
    return res


n = int(input())
d = {}

for i in range(n):
    s = input()
    srtd = get_string(sorted(list(s)))
    if srtd in d:
        d[srtd].append(s)
    else:
        d[srtd] = [s]

for lst in d.values():
    print(*lst)
