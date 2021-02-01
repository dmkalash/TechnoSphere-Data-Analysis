def merge(a, left, mid, right):
    it1, it2 = 0, 0
    res = [0] * (right - left)

    while left + it1 < mid and mid + it2 < right:
        if a[left + it1] < a[mid + it2]:
            res[it1 + it2] = a[left + it1]
            it1 += 1
        else:
            res[it1 + it2] = a[mid + it2]
            it2 += 1

    while left + it1 < mid:
        res[it1 + it2] = a[left + it1]
        it1 += 1

    while mid + it2 < right:
        res[it1 + it2] = a[mid + it2]
        it2 += 1

    for i in range(it1 + it2):
        a[left + i] = res[i]


def merge_sort(a):
    i = 1
    a = [elem for elem in a]
    while i < len(a):
        for j in range(0, len(a) - i, 2 * i):
            merge(a, j, j + i, min(j + 2 * i, len(a)))
        yield a
        i *= 2
