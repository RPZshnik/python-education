import time


def timer(func):
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, '_entered'):
            wrapper._entered = True
            start = time.time()
            result = func(*args, **kwargs)
            work_time = (time.time() - start) * 1000
            print(f'function {func.__name__} finished in {int(work_time)} ms')
            return result
        else:
            return func(*args, **kwargs)
    return wrapper


def cache_decorator(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@timer
@cache_decorator
def fibonacci_cache(n):
    if n <= 1:
        return 1
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)

@timer
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
