  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper