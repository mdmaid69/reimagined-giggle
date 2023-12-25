import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper