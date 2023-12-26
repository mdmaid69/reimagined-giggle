import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread