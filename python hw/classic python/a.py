n = int(input())
a = list(map(int, input().split()))
used = set()
cnt = 0

for el in a:
    if el in used:
        cnt += 1
    else:
        print(el, end=' ')
        used.add(el)

print('\n', cnt, sep='')
