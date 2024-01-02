import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)