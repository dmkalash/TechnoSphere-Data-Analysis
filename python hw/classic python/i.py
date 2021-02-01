import sys


def safe_input():
    try:
        return input()
    except EOFError:
        sys.exit(0)


def get_split(left, r, part):
    step = (r - left + 1) // part
    ost = (r - left + 1) % part
    res = [left]
    for i in range(part):
        left += step
        if ost != 0:
            left += 1
            ost -= 1
        res.append(left - 1)

    return res


l, r = 1, 100000
part = 8
iters = 5

while iters != 0:
    points = get_split(l, r, part)
    for pnt in points[-2:0:-1]:
        print('?', pnt)
    print('+')
    sys.stdout.flush()
    bord_pos = 0
    for i in range(len(points) - 2):
        ans = int(safe_input())
        if not ans and bord_pos == 0:
            bord_pos = part - i - 1

    l, r = points[bord_pos], points[bord_pos + 1]
    iters -= 1


for i in range(r, l, -1):
    print('?', i)
print('+')
sys.stdout.flush()

res = l
for i in range(r, l, -1):
    ans = int(safe_input())
    if not ans and res == l:
        res = i

print('!', res, flush=True)
