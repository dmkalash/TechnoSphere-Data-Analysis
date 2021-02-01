n = int(input())
a = list(map(int, input().split()))

a = sorted(a, key=lambda x: (sum([int(dig) for dig in str(x)]), x))
print(*a)
