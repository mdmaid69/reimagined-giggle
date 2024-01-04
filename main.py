  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper