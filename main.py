  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper