import functools


def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if wrapper.curprop == 0:
            wrapper.ncalls = 0
            wrapper.rdepth = 0
        wrapper.ncalls += 1
        wrapper.curprop += 1
        wrapper.rdepth = max(wrapper.rdepth, wrapper.curprop)
        res = func(*args, **kwargs)
        wrapper.curprop -= 1
        return res

    setattr(wrapper, 'ncalls', 0)
    setattr(wrapper, 'rdepth', 0)
    setattr(wrapper, 'curprop', 0)

    return wrapper


if __name__ == '__main__':
    @counter
    def func1():
        return

    func1()
    print(func1.ncalls, func1.rdepth)

    func1()
    print(func1.ncalls, func1.rdepth)

    @counter
    def func2(n, steps):
        if steps == 0:
            return

        func2(n + 1, steps - 1)
        func2(n - 1, steps - 1)

    func2(0, 5)
    print(func2.ncalls, func2.rdepth)

    func2(0, 3)
    print(func2.ncalls, func2.rdepth)

    print(func2.__name__)
