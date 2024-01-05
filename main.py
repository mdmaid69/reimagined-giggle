import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper