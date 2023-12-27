import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)