a = list(map(int, input().split()))

mn1, mn2 = a[0], a[1]
mx1, mx2 = a[0], a[1]

if a[1] < a[0]:
    mn1, mn2 = a[1], a[0]
else:
    mx1, mx2 = a[1], a[0]

for el in a[2:]:
    if el > mx1:
        mx2 = mx1
        mx1 = el
    elif el > mx2:
        mx2 = el
    if el < mn1:
        mn2 = mn1
        mn1 = el
    elif el < mn2:
        mn2 = el

if (mn1 * mn2, mn1 + mn2) > (mx1 * mx2, mx1 + mx2):
    print(mn1, mn2)
else:
    print(mx2, mx1)
