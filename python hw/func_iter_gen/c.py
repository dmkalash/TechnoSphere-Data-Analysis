import functools
import signal


class TimeoutException(RuntimeError):
    def __init__(self, message=None):
        super().__init__(message)


def timeout(seconds=0.1):
    def decorator(func):
        if not isinstance(seconds, (int, float)) or seconds <= 0:
            return func

        def signal_handler(signal, frame):
            raise TimeoutException("Timed out")

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            old_handler = signal.signal(signal.SIGALRM, signal_handler)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            res = func(*args, **kwargs)
            signal.setitimer(signal.ITIMER_REAL, 0)
            signal.signal(signal.SIGALRM, old_handler)
            return res
        return wrapper
    return decorator


if __name__ == '__main__':
    from time import sleep

    @timeout(seconds=0.5)
    def func():
        sleep(0.1)

    print(func.__name__)

    try:
        func()
    except TimeoutException as e:
        print(e)

    @timeout(seconds=0.5)
    def func():
        sleep(0.6)

    print(func.__name__)

    try:
        func()
    except TimeoutException as e:
        print(e)

    print(func.__name__)

    @timeout(seconds=None)
    def func():
        sleep(0.1)

    print(func.__name__)

    @timeout(seconds=None)
    def func():
        sleep(0.9)

    print(func.__name__)
