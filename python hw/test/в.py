import functools


def retry(check, n_attempts=5):
    if n_attempts is None or n_attempts == 0:
        n_attempts = -1

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            i = 0
            res = None
            ok = False
            while i != n_attempts:
                i += 1
                res = func(*args, **kwargs)
                if check(res):
                    ok = True
                    break
            if not ok:
                raise RuntimeError("Expired number of retries")
            return res
        return wrapper
    return decorator
