import functools
def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
        if args not in cache:
                cache[args] = func(*args)
        return cache[args]
        return wrapper
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)