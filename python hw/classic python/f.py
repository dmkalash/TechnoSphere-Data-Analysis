def check(s2):
    for word in s2:
        if word in d:
            if d[word] == 0:
                return 'NO'
            d[word] -= 1
        else:
            return 'NO'
    return 'YES'


s1 = list(map(str, input().lower().split()))
s2 = list(map(str, input().lower().split()))

d = {}
for word in s1:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(check(s2))
