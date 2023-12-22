  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper