def solution1(arg):
    return [symb * 4 for symb in arg]


def solution2(arg):
    return [arg[i] * (i + 1) for i in range(len(arg))]


def solution3(arg):
    return [elem for elem in arg if elem % 3 == 0 or elem % 5 == 0]


def solution4(arg):
    return [elem for lst in arg for elem in lst]


def solution5(arg):
    return [(a, b, c) for a in range(1, arg - 1) for b in range(a + 1, arg)
            for c in range(b + 1, arg + 1) if a*a + b*b == c*c]


def solution6(arg):
    return [[elem + add for elem in arg[1]] for add in arg[0]]


def solution7(arg):
    return [[arg[i][j] for i in range(len(arg))] for j in range(len(arg[0]))]


def solution8(arg):
    return [list(map(int, s.split())) for s in arg]


def solution9(arg):
    return {chr(ord('a') + d): d * d for d in arg}


def solution10(arg):
    return {s.lower().title() for s in arg if len(s) > 3}


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}


if __name__ == "__main__":
    print(solution1('python'))
    print(solution2('python'))
    print(solution3(range(16)))
    print(solution4([[1, 2, 3], [4, 5, 6, 7], [8, 9], [0]]))
    print(solution5(15))
    print(solution6(([0, 1, 2], [0, 1, 2, 3, 4])))
    print(solution7([[1, 2], [3, 4], [5, 6]]))
    print(solution7([[1, 3, 5], [2, 4, 6]]))
    print(solution8(["0", "1 2 3", "4 5 6 7", "8 9"]))
    print(solution9(range(0, 7)))
    print(solution10(['Alice', 'vova', 'ANTON', 'Bob', 'kAMILA', 'CJ', 'ALICE', 'Nastya']))
