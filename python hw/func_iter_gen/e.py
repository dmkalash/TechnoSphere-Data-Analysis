from itertools import cycle


def chain_loop(args):
    iters = [iter(arg) for arg in args]
    used = [False] * len(iters)
    n = len(iters)
    check = 0

    for i, it in enumerate(cycle(iters)):
        if not used[i % n]:
            try:
                elem = next(it)
            except StopIteration:
                used[i % n] = True
                check += 1
                if check == n:
                    break
            else:
                yield elem


if __name__ == '__main__':
    a = range(5)
    b = range(10)
    c = range(3)

    print(list(chain_loop([a, b, c])))

    a = [None, None, None]
    b = [1] * 5

    print(list(chain_loop([a, b])))

    a = (i for i in range(10))
    b = a

    print(list(chain_loop([a, b])))

    from itertools import tee

    a = (i for i in range(3))

    print(list(chain_loop(tee(a, 5))))
