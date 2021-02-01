from functools import reduce
from operator import add
from operator import setitem
from itertools import chain


def solution1(arg):
    return list(map(
        lambda s: int(reduce(add, list((filter(
            lambda sym: sym.isdigit(), s))))[::-1]), arg))


def solution2(arg):
    return [pair[0] * pair[1] for pair in arg]


def solution3(arg):
    return list(filter(lambda x: x % 6 in [0, 2, 5], arg))


def solution4(arg):
    return list(filter(None, arg))


def solution5(arg):
    return list(map(lambda d:
                    setitem(d, 'square', d['width'] * d['length']), arg))


def solution6(arg):
    return list(map(
        lambda d: dict(chain(d.items(),
                             [('square', d['width'] * d['length'])])), arg))


def solution7(arg):
    return reduce(set.intersection, arg)


def solution8(arg):
    return reduce(
        lambda prev, cur:
            setitem(prev, cur, prev.get(cur, 0) + 1) or prev, arg, {})


def solution9(arg):
    return list(map(
        lambda x: x['name'], filter(lambda d: d['gpa'] > 4.5, arg)))


def solution10(arg):
    return list(filter(
        lambda x: sum(map(int, x[slice(0, None, 2)])) ==
                sum(map(int, x[slice(1, None, 2)])), arg))


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
    print(solution1(['12', '25.6', '84,02', '  69-91']))
    print(solution2(zip(range(2, 5), range(3, 9, 2))))
    print(solution3(range(20)))
    print(solution4(['', 25, None, 'python', 0.0, [], ('msu', '1755-01-25')]))

    rooms = [
        {"name": "комната1", "width": 2, "length": 4},
        {"name": "комната2", "width": 2.5, "length": 5.6},
        {"name": "кухня", "width": 3.5, "length": 4},
        {"name": "туалет", "width": 1.5, "length": 1.5},
    ]
    solution5(rooms)
    print(rooms, '\n')

    rooms = [
        {"name": "комната1", "width": 2, "length": 4},
        {"name": "комната2", "width": 2.5, "length": 5.6},
        {"name": "кухня", "width": 3.5, "length": 4},
        {"name": "туалет", "width": 1.5, "length": 1.5},
    ]

    print(solution6(rooms))
    print(rooms, '\n')

    print(solution7([{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}, {3, 4, 5, 6, 7}]))
    print(solution8([1, 2, 1, 1, 3, 2, 3, 2, 4, 2, 4]))

    students = [
        {'name': 'Alina', 'gpa': 4.57},
        {'name': 'Sergey', 'gpa': 5.0},
        {'name': 'Nastya', 'gpa': 4.21},
        {'name': 'Valya', 'gpa': 4.72},
        {'name': 'Anton', 'gpa': 4.32},
    ]

    print(solution9(students))

    print(solution10(['165033', '477329', '631811', '478117',
                      '475145', '238018', '917764', '394286']))
